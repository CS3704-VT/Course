# Evidence-Based Software Engineering --- Benchmarking LLMs and Mining GitHub

Software engineering is full of claims about what makes development "better", and even moreso now that AI tools are taking over how code is written and maintained. Very few of these claims have been backed by strong evidence. In this activity, you will work in a group to gain experience gathering software engineering-related evidence. In **Phase 1**, you will benchmark an LLM on small coding tasks, watch how much the results change from run to run, and examine the benchmark itself. In **Phase 2**, you will learn about the GitHub API and use it to answer questions about real codebases. 

## Setup

For this activity, you will need Python 3, a GitHub token, and an ARC API key. Run all commands from the root of your clone of the course repository.

**Scripts**
    - Download the [`llmbench.py`](https://github.com/CS3704-VT/Course/blob/main/resources/llmbench.py) and [`mine.py`](https://github.com/CS3704-VT/Course/blob/main/resources/mine.py) Python scripts from the Course repository into the directory where you will complete this activity. You will not need to modify them for this assignment.

**GitHub token** 
    - Create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) with **public repository read-only** access. If your Project 2 repository is private, also grant the token read access to that repository (fine-grained tokens let you select specific repositories).
    - Set it in your terminal: `export GITHUB_TOKEN=<your token>` (Windows PowerShell: `$env:GITHUB_TOKEN="<your token>"`).
    - Verify: `python3 mine.py commits CS3704-VT/Course --limit 5` # prints five most recent commits

**ARC API key** 
    - You should have set up an ARC API Key environment variable in [PM0](../../Projects/Project0/PM0.0.md).
    - Verify: `python3 llmbench.py --dry-run` (checks the test suite locally), then verify one real run: `python3 llmbench.py --runs 1`

:warning: **Never commit your tokens or API keys!** Sharing your API key is a violation of university policy.

## Initial Activity

_Reflection:_ As a group, discuss the following:

* How do you decide whether or not to adopt a new model or AI-based tool? To what extent do results from popular benchmarks, social media, cost, etc. play into your decision?

## Phase 1: Benchmarking an LLM

[HW4](../../HWs/HW4.md) will focus on how to respond to claims regarding AI in software development workflows. This activity will provide practical experience with a simple benchmarking task to observe the challenges with this approach discussed in the lecture. The [starter script](../llmbench.py) (Python standard library only) sends five programming tasks to the course LLM API, each with a short prompt and a set of unit tests the model never sees:

| Task | What it asks for |
| --- | --- |
| `letter_grade` | Convert a course score to a letter grade using a syllabus scale |
| `fix_last` | Debug a function that should return the last index of an item |
| `binary_search` | Implement binary search over a sorted list |
| `password_rules` | Check a password against length, character, and whitespace rules |
| `playlist` | Implement a small class that adds, removes, and counts song titles |

A task counts as passed only if the answer passes every one of its tests.

### 1a: Run the benchmark

```sh
python3 llmbench.py --runs 10 > llmbench.csv
```

Each run attempts all five tasks, and each attempt passes or fails. Every generated answer is saved under `llmbench-output/`, prefixed with the model and run (for example, `DeepSeek-V4.1-Flash-run01-task1-letter_grade.txt`), so you can compare attempts directly. A summary is printed to the terminal: per-run scores, the mean/median/min/max, and per-task pass rates. A full benchmark makes 50 API calls and can take a while --- start it, then begin Phase 2a while it runs.

Notes:
- The default model is `DeepSeek-V4.1-Flash`. To compare models in one command, comma-separate names: `--model DeepSeek-V4.1-Flash,GLM-5.3` (also available: `gpt-oss-120b`). Each extra model doubles the number of API calls, so compare with `--runs 5` if time is tight.
- The script uses each model's default sampling settings. Note this when you discuss validity: what would you expect at a temperature of zero?
- You may modify the tasks, prompts, or number of runs (with or without AI help). Record any changes you make.

### 1b: Examine the benchmark itself

A benchmark is a dataset too: the tasks, the prompts, and the tests decide what "passing" means. Open `llmbench.py`, read the five task definitions and their checks, then:

1. For each task, write one sentence on what the tests actually measure (for example: handling boundary values, following a specification exactly, designing a small class).
2. Find one weakness in the benchmark as a measure of coding ability. For example: an edge case the tests never check, a reasonable answer that would fail, a wrong answer that would pass, or a prompt that is ambiguous.
3. Which task varies the most across runs? Which is most stable?
4. Decide: if a vendor reported only the mean per-run score from this benchmark, what would that number hide?

_Analysis:_

1. Using `llmbench.csv`, compute each run's score (0-5), then the mean, median, minimum, and maximum across runs. How wide is the range? If you ran two models, compare their distributions.
2. Summarize your findings and compare with others in your group. Then write down your thoughts on the **threats to validity**, or limitations, of this benchmarking strategy. Some potential topics to discuss include:
    - _Construct validity:_ do five toy Python tasks measure "coding ability"? What does a pass/fail count miss (code quality? security? readability?)
    - _Internal validity:_ prompt wording, sampling settings, server-side caching --- what else could explain run-to-run or model-to-model differences?
    - _External validity:_ would your conclusion hold for other models, languages, or real project tasks like your Project 2 work?

## Phase 2: Mining Software Repositories

### What is an API?

Application Programming Interfaces (APIs) define a specification for how to communicate with a computer program. An API lays out what functionality is offered, what parameters must be provided when making calls, and provides some guarantees about the return type given the preconditions are satisfied. APIs were also one of the most-reported gaps in our department's curriculum from students participating in the [CS@VT Internship Symposium](https://chbrown13.github.io/files/posters/Intern_Symposium.pdf)

A _REST API_ is a subtype of APIs that is geared towards Internet-facing systems. The goal of REST APIs is to provide painless communication and interoperability between these Internet-facing applications and systems. REST APIs typically allow (often with some sort of authentication) a manipulation of the various types of entities (recipes, inventory, etc) that a web application revolves around.[^1]

Typically, REST API operations are carried out over HTTP. The actions most commonly available are:

| HTTP Verb	| Action             |	Example	       |Result  | 
| --------- | ------------------ | --------------- |------- |
| GET	    | Retrieve record(s) | GET /users/	   | Retrieves all users|
| DELETE	| Delete record(s)	 | DELETE /users/1 | Deletes user with id 1|
| POST	    | Create record	     | POST /users/	   | Creates a new user|
| PUT	    | Update record	     | PUT /users/6	   | Updates user 6|

## Practicing with a REST Client

### 2a: The GitHub API

1. Open <https://api.github.com/repos/microsoft/vscode> in your browser. You are looking at the same data the VS Code project page displays, as raw JSON. Find `stargazers_count`, `created_at`, `pushed_at`, `license`, `default_branch`, and `open_issues_count`.
2. From the terminal, `curl https://api.github.com/repos/microsoft/vscode` returns the same JSON. A web API is just an HTTP request that returns structured data. (Windows: please use `curl.exe` instead of `curl`)
3. Rate limits: run `curl https://api.github.com/rate_limit`, then run it again with your token (below) and compare the limits with and without authentication.

    ```sh
    curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/rate_limit [Linux/Mac]
    curl.exe -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/rate_limit [Windows]
    ```

4. Pagination: APIs return data in pages. Run `curl -I "https://api.github.com/repos/microsoft/vscode/commits?per_page=5&page=2"` and find the `Link` response header, which points to the next and last pages.

### 2b: The state of VS Code

Answer these questions about `microsoft/vscode` --- the repository of the editor you are typing these commands in --- using `curl` and the [starter script](../mine.py). Include the commands you used.

1. How old is the project, and when was the last push? Would you call it maintained? (`/repos/microsoft/vscode`)
2. Who are the top contributors, and how many contributions do they have? (`/repos/microsoft/vscode/contributors?per_page=10`)
3. What fraction of the last 100 commits carry an AI co-author trailer (e.g., `Co-authored-by: Copilot`)? What is the average *code churn* (`lines_changed` = additions + deletions) and *files changed* with and without an AI co-author? (`python3 mine.py commits microsoft/vscode --limit 100 > vscode_commits.csv`; see `ai_coauthor_trailer` column; open `vscode_commits.csv` in Excel or another spreadsheet application for a better view)
4. Do pull requests that change test files take longer to merge than those that don't? (`python3 mine.py prs microsoft/vscode --limit 30`; see `touches_tests` and `hours_to_merge` columns)

### 2c: Your Project 2 repository

Now point the same tools at your own repository:

```sh
python3 mine.py prs <owner>/<repo> --limit 30 > p2-prs.csv
python3 mine.py issues <owner>/<repo> --limit 30 > p2-issues.csv
python3 mine.py commits <owner>/<repo> --limit 100 > p2-commits.csv
```

1. How long do your pull requests stay open? Do test-touching PRs differ from the rest?
2. What fraction of your commits carry AI co-author trailers? Does that match how much AI your team actually used? If not, what does that say about the measurement (it only detects _disclosed_ AI use)? In general, how does your AI usage compare with your findings from the VS Code repository?
3. How many people wrote most of your code? How quickly did issues and pull requests get responses?
4. Where do these numbers disagree with how the sprint _felt_? Which do you trust more, and why?
5. Come up with another question to ask about your codebase or development processes. Write down your question, your prediction, the command/data used to answer the question, the result, and how the outcome compared with your initial intuition.

## Reflection

_Each student will **individually**_ post in the class Mattermost channel: (1) a benchmark headline --- one main takeaway from the benchmarking activity; (2) one finding from VS Code or your Project 2 repository that surprised you; and (3) a reflection on what evidence would influence decision making for development tasks. Some ideas to start with include:

- Is a single benchmark run enough to report a model's performance?
- Would you trust a benchmark's headline number? Why or why not?
- What was most interesting about the development processes for VS Code?
- Did your Project 2 numbers match how the project actually felt?
- What would it take for you to trust an answer enough to change how a team works?


**Submission**: Upload one document per group on Canvas with: (1) a summary of your initial discussion; (2) your benchmark analysis, results, and threats; (3) your VS Code answers with the commands you used; and (4) your Project 2 repository mining findings.

**Due:** Thursday, November 19 at 11:59pm

---
## References

[^1] Content based on the [Onboarding-REST](https://github.com/CSC-326/Onboarding-REST) workshop by Dr. Chris Parnin. 