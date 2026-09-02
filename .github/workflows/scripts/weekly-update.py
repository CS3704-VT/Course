#!/usr/bin/env python3
"""Parse the Course README schedule and post a weekly Mattermost update.

Reads README.md, finds HW/PM items with "due M/D" dates and exams (midterm/final)
in the schedule table, then posts a message listing those falling in the current
Mon-Fri week (in the course timezone, America/New_York).

Usage:
    python scripts/mattermost_weekly.py                        # post to webhook
    python scripts/mattermost_weekly.py --dry-run              # print message only
    python scripts/mattermost_weekly.py --date 2026-09-14 --dry-run  # test a past week
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

README_PATH = os.environ.get("COURSE_README", "README.md")
TIMEZONE = os.environ.get("COURSE_TZ", "America/New_York")
WEBHOOK_URL = os.environ.get("MATTERMOST_WEBHOOK_URL", "")
BOT_NAME = os.environ.get("MATTERMOST_USERNAME", "CourseBot")
REPO = os.environ.get("COURSE_REPO", "CS3704-VT/Course")
BRANCH = os.environ.get("COURSE_BRANCH", "main")
GITHUB_BASE = f"https://github.com/{REPO}/blob/{BRANCH}"

ASSIGNMENT_RE = re.compile(r"HW\d+|PM\d+\.\d+(?:\.\d+)?")
LINK_RE = re.compile(r"\[(HW\d+|PM\d+\.\d+(?:\.\d+)?)\]\(([^)]+)\)")
DUE_DATE_RE = re.compile(r"due\s+(\d{1,2})[/-](\d{1,2})", re.IGNORECASE)
DATE_CELL_RE = re.compile(
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\s+(\d{1,2})",
    re.IGNORECASE)
EXAM_TOPIC_RE = re.compile(r"\bExam\b", re.IGNORECASE)
REVIEW_RE = re.compile(r"\bReview\b|\bWorkday\b", re.IGNORECASE)

MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
          7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
MONTH_NAMES = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
               "jul": 7, "aug": 8, "sept": 9, "sep": 9, "oct": 10, "nov": 11,
               "dec": 12}


def resolve_link(link):
    """Convert a README-relative link to a browser-openable GitHub URL."""
    if link.startswith(("http://", "https://")):
        return link
    return f"{GITHUB_BASE}/{link.lstrip('./')}"


def parse_schedule(readme_path, year):
    """Return [(kind, name, due_date, link), ...] from the schedule table.

    kind is "assignment" (HW/PM) or "exam" (midterm/final). A cell like
    "PM1.0, HW0 due 9/4" assigns that date to every assignment in the cell.
    """
    with open(readme_path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    items = []
    seen = set()
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if len(cells) < 3:  # skips footer/separator/section-header rows
            continue
        date_cell, topic_cell, assign_cell = cells[0], cells[1], cells[2]

        if assign_cell:
            links = dict(LINK_RE.findall(assign_cell))
            for month, day in DUE_DATE_RE.findall(assign_cell):
                try:
                    due = dt.date(year, int(month), int(day))
                except ValueError:
                    continue
                for name in ASSIGNMENT_RE.findall(assign_cell):
                    key = ("assignment", name, due)
                    if key in seen:
                        continue
                    seen.add(key)
                    items.append(("assignment", name, due, links.get(name)))

        if EXAM_TOPIC_RE.search(topic_cell) and not REVIEW_RE.search(topic_cell):
            m = DATE_CELL_RE.search(date_cell)
            if m:
                due = dt.date(year, MONTH_NAMES[m.group(1).lower()],
                              int(m.group(2)))
                name = "Final Exam" if "Final" in topic_cell else "Midterm Exam"
                key = ("exam", name, due)
                if key not in seen:
                    seen.add(key)
                    items.append(("exam", name, due, None))

    items.sort(key=lambda t: (t[2], t[0]))
    return items


def week_of(ref_date):
    """Return (monday, friday) dates for the Mon-Fri span with ref_date."""
    monday = ref_date - dt.timedelta(days=ref_date.weekday())
    return monday, monday + dt.timedelta(days=4)


def format_date(d):
    return f"{d.strftime('%a')} {MONTHS[d.month]} {d.day}"


def format_range(start, end):
    s = f"{MONTHS[start.month]} {start.day}"
    e = f"{MONTHS[end.month]} {end.day}, {end.year}"
    return s if start == end else f"{s}\u2013{e}"


def build_message(items, monday, friday):
    lines = [f"##### \U0001f4c5 Weekly CS3704 Update\n> ##### Week of "
             f"{format_range(monday, friday)}", ""]
    if items:
        lines.append("**Assignments due this week (Mon\u2013Fri):**")
        lines.append("")
        for kind, name, due, link in items:
            if kind == "exam":
                lines.append(f"- **{name}** \u2014 **{format_date(due)}**")
            else:
                name_fmt = (f"[{name}]({resolve_link(link)})"
                            if link else f"**{name}**")
                lines.append(f"- {name_fmt} \u2014 due **{format_date(due)}**")
    else:
        lines.append("\U0001f389 No assignments or exams this week!")
    lines.append("")
    lines.append(f"*Source: [Course README]({resolve_link('README.md')})*")
    return "\n".join(lines)


def post_webhook(message, dry_run):
    if dry_run:
        print(message)
        return 0
    if not WEBHOOK_URL:
        print("ERROR: MATTERMOST_WEBHOOK_URL is not set "
              "(use --dry-run to preview).", file=sys.stderr)
        return 2
    payload = json.dumps({"text": message, "username": BOT_NAME}).encode("utf-8")
    req = urllib.request.Request(WEBHOOK_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return 0 if 200 <= resp.status < 300 else 1
    except urllib.error.HTTPError as exc:
        print(f"Webhook failed: HTTP {exc.code}: "
              f"{exc.read().decode(errors='replace')}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 - surface any network error
        print(f"Webhook request failed: {exc}", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Treat YYYY-MM-DD as today (testing)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the message instead of posting it")
    args = parser.parse_args()

    if args.date:
        ref_date = dt.date.fromisoformat(args.date)
    else:
        ref_date = dt.datetime.now(ZoneInfo(TIMEZONE)).date()

    items = parse_schedule(README_PATH, year=ref_date.year)
    monday, friday = week_of(ref_date)
    due_this_week = [i for i in items if monday <= i[2] <= friday]
    message = build_message(due_this_week, monday, friday)
    sys.exit(post_webhook(message, args.dry_run))


if __name__ == "__main__":
    main()

