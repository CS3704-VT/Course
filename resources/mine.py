#!/usr/bin/env python3
"""Mine GitHub data into a CSV for the CS3704 evidence-based SE activity.

Usage:
  export GITHUB_TOKEN=<your token>      # or: export GITHUB_TOKEN=$(gh auth token)
  python3 resources/mine.py prs     owner/repo [owner/repo ...] --limit 30 > prs.csv
  python3 resources/mine.py issues  owner/repo [owner/repo ...] --limit 30 > issues.csv
  python3 resources/mine.py commits owner/repo [owner/repo ...] --limit 200 > commits.csv

The commits command also fetches each commit's detail (~1 extra API call per commit)
to include line counts and file-status counts.
"""
import argparse, csv, json, os, re, sys, urllib.request
from collections import Counter
from datetime import datetime

API = "https://api.github.com"
TEST_PATH = re.compile(r"(^|/)(tests?|__tests__|spec)(/|$)|(^|/)test_[^/]*$|_test\.|\.test\.|\.spec\.", re.I)
AI_TRAILER = re.compile(r"co-authored-by:.*(claude|copilot|chatgpt|openai|cursor|devin|gemini|codex)", re.I)


def get(path):
    req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        left = resp.headers.get("X-RateLimit-Remaining")
        if left is not None and int(left) < 20:
            print(f"warning: only {left} API calls left this hour", file=sys.stderr)
        return json.load(resp)


def hours(start, end):
    if not start or not end:
        return ""
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return round((datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).total_seconds() / 3600, 2)


def mine_prs(repo, limit):
    pulls = get(f"/repos/{repo}/pulls?state=closed&per_page={min(limit, 100)}")[:limit]
    for p in pulls:
        if not p["merged_at"]:
            continue  # closed without merging
        detail = get(f"/repos/{repo}/pulls/{p['number']}")
        files = get(f"/repos/{repo}/pulls/{p['number']}/files?per_page=100")
        yield {
            "repo": repo,
            "number": p["number"],
            "author_association": p["author_association"],
            "additions": detail["additions"],
            "deletions": detail["deletions"],
            "changed_files": detail["changed_files"],
            "touches_tests": any(TEST_PATH.search(f["filename"]) for f in files),
            "comments": detail["comments"] + detail["review_comments"],
            "hours_to_merge": hours(p["created_at"], p["merged_at"]),
        }


def mine_issues(repo, limit):
    issues = get(f"/repos/{repo}/issues?state=all&per_page=100")
    issues = [i for i in issues if "pull_request" not in i][:limit]
    for i in issues:
        first = ""
        if i["comments"]:
            comments = get(f"/repos/{repo}/issues/{i['number']}/comments?per_page=30")
            others = [c for c in comments if c["user"]["login"] != i["user"]["login"]]
            first = others[0]["created_at"] if others else ""
        yield {
            "repo": repo,
            "number": i["number"],
            "author_association": i["author_association"],
            "state": i["state"],
            "comments": i["comments"],
            "hours_to_first_response": hours(i["created_at"], first),
            "hours_to_close": hours(i["created_at"], i["closed_at"]),
        }


def mine_commits(repo, limit):
    seen, page = 0, 1
    while seen < limit:
        batch = get(f"/repos/{repo}/commits?per_page=100&page={page}")
        if not batch:
            return
        for c in batch[: limit - seen]:
            msg = c["commit"]["message"]
            heading = next((line.strip() for line in msg.splitlines() if line.strip()), "")
            detail = get(f"/repos/{repo}/commits/{c['sha']}")
            stats = detail.get("stats") or {}
            files = detail.get("files") or []
            additions = stats.get("additions", 0)
            deletions = stats.get("deletions", 0)
            statuses = Counter(f.get("status", "") for f in files)
            tracked = ("added", "removed", "modified", "renamed")
            other = len(files) - sum(statuses.get(status, 0) for status in tracked)
            if len(files) == 300:
                print(f"warning: commit {c['sha'][:10]} has 300 files; GitHub paginates beyond this", file=sys.stderr)
            yield {
                "repo": repo,
                "sha": c["sha"][:10],
                "date": c["commit"]["author"]["date"],
                "message_heading": heading,
                "ai_coauthor_trailer": bool(AI_TRAILER.search(msg)),
                "any_coauthor_trailer": "co-authored-by:" in msg.lower(),
                "additions": additions,
                "deletions": deletions,
                "lines_changed": stats.get("total", additions + deletions),
                "changed_files": len(files),
                "files_added": statuses.get("added", 0),
                "files_removed": statuses.get("removed", 0),
                "files_modified": statuses.get("modified", 0),
                "files_renamed": statuses.get("renamed", 0),
                "files_other": max(other, 0),
            }
        seen += len(batch)
        page += 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["prs", "issues", "commits"])
    ap.add_argument("repos", nargs="+", help="owner/repo")
    ap.add_argument("--limit", type=int, default=30, help="items per repo")
    args = ap.parse_args()
    if not os.environ.get("GITHUB_TOKEN"):
        print("warning: no GITHUB_TOKEN set; you get only 60 API calls per hour", file=sys.stderr)
    miner = {"prs": mine_prs, "issues": mine_issues, "commits": mine_commits}[args.kind]
    writer = None
    for repo in args.repos:
        for row in miner(repo, args.limit):
            if writer is None:
                writer = csv.DictWriter(sys.stdout, fieldnames=row.keys())
                writer.writeheader()
            writer.writerow(row)


if __name__ == "__main__":
    main()
