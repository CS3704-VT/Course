#!/usr/bin/env python3
"""Benchmark an LLM on small coding tasks for the CS3704 evidence-based SE activity.

Usage:
  export ARC_API_KEY=<your key>      # from https://www.docs.arc.vt.edu/ai/011_llm_api_arc_vt_edu.html
  python3 resources/llmbench.py --runs 10 > llmbench.csv
  python3 resources/llmbench.py --runs 5 --model DeepSeek-V4.1-Flash,GLM-5.3 > llmbench.csv
  python3 resources/llmbench.py --dry-run    # verify the test harness locally, no API calls

Each run sends every task to the model and scores the answer against unit tests.
Pass several comma-separated model names to --model to compare models in one
invocation. Raw model answers are saved under --out-dir, prefixed with the model
name, so attempts from different runs and models can be compared directly.
Progress and per-model summaries (run scores and per-task pass rates) go to stderr.
"""
import argparse, csv, json, os, re, subprocess, sys, tempfile, time, urllib.request
from statistics import mean, median

API = os.environ.get("ARC_API_BASE", "https://llm-api.arc.vt.edu/api/v1")
RUNNER = """

import json as _json

_results = []
for _name, _fn in sorted(list(globals().items())):
    if _name.startswith("test_") and callable(_fn):
        try:
            _fn()
            _results.append(True)
        except Exception:
            _results.append(False)
print(_json.dumps(_results))
"""

TASKS = [
    {
        "name": "letter_grade",
        "prompt": """Write a single Python function `letter_grade(score)` that converts a numeric course score (0-100, possibly a float) into the course letter grade:

93 or above: A
90 to 92.99: A-
87 to 89.99: B+
83 to 86.99: B
80 to 82.99: B-
77 to 79.99: C+
73 to 76.99: C
70 to 72.99: C-
65 to 69.99: D
below 65: F

Examples:
letter_grade(95) == "A"
letter_grade(92.5) == "A-"
letter_grade(85) == "B"
letter_grade(64.9) == "F"

Reply with only the function definition inside one Python code block. No tests, no explanation.""",
        "reference": """def letter_grade(score):
    if score >= 93:
        return "A"
    if score >= 90:
        return "A-"
    if score >= 87:
        return "B+"
    if score >= 83:
        return "B"
    if score >= 80:
        return "B-"
    if score >= 77:
        return "C+"
    if score >= 73:
        return "C"
    if score >= 70:
        return "C-"
    if score >= 65:
        return "D"
    return "F"
""",
        "checks": [
            'assert letter_grade(95) == "A"',
            'assert letter_grade(100) == "A"',
            'assert letter_grade(93) == "A"',
            'assert letter_grade(92.9) == "A-"',
            'assert letter_grade(90) == "A-"',
            'assert letter_grade(87) == "B+"',
            'assert letter_grade(85) == "B"',
            'assert letter_grade(80) == "B-"',
            'assert letter_grade(77) == "C+"',
            'assert letter_grade(75) == "C"',
            'assert letter_grade(70) == "C-"',
            'assert letter_grade(65) == "D"',
            'assert letter_grade(64.9) == "F"',
            'assert letter_grade(0) == "F"',
        ],
    },
    {
        "name": "fix_last",
        "prompt": """This Python function should return the index of the LAST occurrence of `target` in `items`, or -1 if there is none, but it has a bug:

```python
def find_last(items, target):
    found = -1
    for i in range(len(items) - 1):
        if items[i] == target:
            found = i
    return found
```

Fix the bug. Keep the same function name and signature.

Examples:
find_last(["a", "b", "a"], "a") == 2
find_last([1, 2, 3], 3) == 2
find_last([1, 2], 9) == -1

Reply with only the corrected function definition inside one Python code block. No tests, no explanation.""",
        "reference": """def find_last(items, target):
    found = -1
    for i in range(len(items)):
        if items[i] == target:
            found = i
    return found
""",
        "checks": [
            'assert find_last(["a", "b", "a"], "a") == 2',
            'assert find_last([1, 2, 3], 3) == 2',
            'assert find_last([1, 2], 9) == -1',
            'assert find_last([], 1) == -1',
            'assert find_last([7], 7) == 0',
            'assert find_last([4, 4, 4], 4) == 2',
        ],
    },
    {
        "name": "binary_search",
        "prompt": """Write a single Python function `binary_search(numbers, target)`. `numbers` is a list of integers sorted in ascending order and contains no duplicates.
- Return the index of `target` if it is present, otherwise -1.
- Use binary search: do not scan the whole list from the front.

Examples:
binary_search([1, 3, 5, 7, 9], 7) == 3
binary_search([1, 3, 5], 1) == 0
binary_search([1, 3, 5], 4) == -1
binary_search([], 2) == -1

Reply with only the function definition inside one Python code block. No tests, no explanation.""",
        "reference": """def binary_search(numbers, target):
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
""",
        "checks": [
            'assert binary_search([1, 3, 5, 7, 9], 7) == 3',
            'assert binary_search([1, 3, 5], 1) == 0',
            'assert binary_search([1, 3, 5], 5) == 2',
            'assert binary_search([1, 3, 5], 4) == -1',
            'assert binary_search([], 2) == -1',
            'assert binary_search([10], 10) == 0',
        ],
    },
    {
        "name": "password_rules",
        "prompt": """Write a single Python function `is_strong_password(pw)` that returns True only if `pw`:
- is at least 10 characters long,
- contains at least one uppercase letter, one lowercase letter, and one digit,
- contains no whitespace characters.

Examples:
is_strong_password("Abcdef1234") == True
is_strong_password("abcdef1234") == False
is_strong_password("Abcdefghij") == False
is_strong_password("Abcdef123") == False

Reply with only the function definition inside one Python code block. No tests, no explanation.""",
        "reference": """def is_strong_password(pw):
    if len(pw) < 10:
        return False
    if any(c.isspace() for c in pw):
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    return has_upper and has_lower and has_digit
""",
        "checks": [
            'assert is_strong_password("Abcdef1234") == True',
            'assert is_strong_password("Abcdef12345") == True',
            'assert is_strong_password("Abcdefg1!x") == True',
            'assert is_strong_password("abcdef1234") == False',
            'assert is_strong_password("ABCDEFGHIJ1") == False',
            'assert is_strong_password("Abcdefghij") == False',
            'assert is_strong_password("Abcdef123") == False',
            'assert is_strong_password("Abc def1234") == False',
            'assert is_strong_password("Abcd\\t1234X") == False',
        ],
    },
    {
        "name": "playlist",
        "prompt": """Write a Python class `Playlist`:
- `Playlist()` starts empty.
- `add(title)` appends a title; if the exact same title is already in the playlist, adding it again does nothing.
- `remove(title)` removes the title if present; removing an unknown title does nothing.
- `titles` returns a list of the titles in playlist order (the order they were added).
- `len(playlist)` returns how many distinct titles the playlist holds.

Examples:
p = Playlist()
p.add("Song A")
p.add("Song A")
p.add("Song B")
p.titles == ["Song A", "Song B"]
len(p) == 2
p.remove("Song A")
p.titles == ["Song B"]
p.add("Song A")
p.titles == ["Song B", "Song A"]

Reply with only the class definition inside one Python code block. No tests, no explanation.""",
        "reference": """class Playlist:
    def __init__(self):
        self._titles = []

    def add(self, title):
        if title not in self._titles:
            self._titles.append(title)

    def remove(self, title):
        if title in self._titles:
            self._titles.remove(title)

    @property
    def titles(self):
        return list(self._titles)

    def __len__(self):
        return len(self._titles)
""",
        "checks": [
            "p = Playlist(); assert len(p) == 0",
            'p = Playlist(); p.add("A"); p.add("A"); assert p.titles == ["A"] and len(p) == 1',
            'p = Playlist(); p.add("A"); p.add("B"); assert p.titles == ["A", "B"]',
            'p = Playlist(); p.add("A"); p.remove("A"); assert p.titles == [] and len(p) == 0',
            'p = Playlist(); p.add("A"); p.remove("Z"); assert p.titles == ["A"]',
            'p = Playlist(); [p.add(t) for t in ["B", "A", "C"]]; p.remove("A"); p.add("A"); assert p.titles == ["B", "C", "A"]',
        ],
    },
]


def chat(prompt, model, key):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}]}).encode()
    last_error = None
    for _ in range(2):
        req = urllib.request.Request(
            API.rstrip("/") + "/chat/completions",
            data=body,
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.load(resp)
            return data["choices"][0]["message"]["content"]
        except Exception as exc:
            last_error = exc
            time.sleep(2)
    raise last_error


def extract_code(text):
    match = re.search(r"```(?:python|py)?\s*\n(.*?)```", text, re.S | re.I)
    return match.group(1) if match else text


def tests_source(checks):
    return "\n\n".join(f"def test_{i}():\n    {check}" for i, check in enumerate(checks, 1))


def score_attempt(code, task):
    total = len(task["checks"])
    source = code + "\n\n\n" + tests_source(task["checks"]) + RUNNER
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "attempt.py")
        with open(path, "w") as handle:
            handle.write(source)
        try:
            proc = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=20)
        except subprocess.TimeoutExpired:
            return 0, total, "timeout"
    lines = proc.stdout.strip().splitlines()
    if not lines:
        error = (proc.stderr.strip().splitlines() or ["unknown error"])[-1]
        return 0, total, error[:200]
    try:
        results = json.loads(lines[-1])
    except json.JSONDecodeError:
        return 0, total, "could not parse test output"
    return sum(1 for result in results if result), total, ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=int, default=10, help="runs per task per model (default 10)")
    ap.add_argument("--model", default="DeepSeek-V4.1-Flash",
                    help="ARC model name(s), comma-separated to compare (default DeepSeek-V4.1-Flash)")
    ap.add_argument("--out-dir", default="llmbench-output", help="directory for raw model answers (default llmbench-output)")
    ap.add_argument("--dry-run", action="store_true", help="score the reference solutions locally; no API calls")
    args = ap.parse_args()

    if args.dry_run:
        failed = False
        for task in TASKS:
            passed, total, error = score_attempt(task["reference"], task)
            status = "ok" if passed == total else f"FAILED ({error})"
            print(f"{task['name']}: {passed}/{total} tests {status}")
            failed = failed or passed != total
        sys.exit(1 if failed else 0)

    key = os.environ.get("ARC_API_KEY")
    if not key:
        print("error: set ARC_API_KEY (see the activity's Setup section)", file=sys.stderr)
        sys.exit(1)

    models = [name.strip() for name in args.model.split(",") if name.strip()]
    if not models:
        print("error: --model needs at least one model name", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.out_dir, exist_ok=True)
    writer = csv.DictWriter(
        sys.stdout, fieldnames=["run", "task", "model", "tests_passed", "tests_total", "passed", "error"]
    )
    writer.writeheader()

    for model in models:
        scores = []
        task_passes = {task["name"]: 0 for task in TASKS}
        safe_model = re.sub(r"[^A-Za-z0-9._-]+", "-", model)
        for run in range(1, args.runs + 1):
            run_score = 0
            for index, task in enumerate(TASKS, 1):
                answer, error = "", ""
                try:
                    answer = chat(task["prompt"], model, key)
                except Exception as exc:
                    error = f"api error: {exc}"
                if answer:
                    filename = f"{safe_model}-run{run:02d}-task{index}-{task['name']}.txt"
                    with open(os.path.join(args.out_dir, filename), "w") as handle:
                        handle.write(answer)
                    passed, total, check_error = score_attempt(extract_code(answer), task)
                    error = error or check_error
                else:
                    passed, total = 0, len(task["checks"])
                ok = passed == total and not error
                if ok:
                    run_score += 1
                    task_passes[task["name"]] += 1
                writer.writerow({
                    "run": run,
                    "task": task["name"],
                    "model": model,
                    "tests_passed": passed,
                    "tests_total": total,
                    "passed": ok,
                    "error": error,
                })
            scores.append(run_score)
            print(f"[{model}] run {run}/{args.runs}: {run_score}/{len(TASKS)} tasks passed", file=sys.stderr)

        per_task = " | ".join(f"{name} {count}/{args.runs}" for name, count in task_passes.items())
        print(f"\nmodel: {model}", file=sys.stderr)
        print(f"per-run scores: {scores}", file=sys.stderr)
        print(f"task pass rates: {per_task}", file=sys.stderr)
        print(
            f"mean {mean(scores):.2f} | median {median(scores):.2f} | "
            f"min {min(scores)} | max {max(scores)} | distinct scores {sorted(set(scores))}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
