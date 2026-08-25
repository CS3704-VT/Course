# Project Milestone 0.0: CS3704 Agentic Environment Setup 

Each student must install, configure, and verify the software, tools, and dependencies required for development. The purpose of this assignment is to ensure that every student has a working environment and can participate in the project and course assignments this semester. This also reflects real software development work, where configuring environments is necessary yet a major challenge in practice. The course tools below aim to make this process easier for students.

---

## 0. Before you start

You need `git` and Node.js 18+.

```sh
git --version
node --version
npm --version
```

Get an ARC API key from [llm.arc.vt.edu](https://llm.arc.vt.edu) → *Settings → Account → API keys*:

```sh
export ARC_API_KEY=sk-...     # macOS / Linux — add to ~/.bashrc or ~/.zshrc
setx ARC_API_KEY sk-...       # Windows — then open a NEW terminal
```

Check it survives a new terminal:

```sh
echo $ARC_API_KEY             # macOS / Linux
echo %ARC_API_KEY%            # Windows
```

---

## 1. Install Baker

```sh
git clone https://github.com/chbrown13/Baker
cd Baker
npm install
npm link
baker --version
```

`npm link` points at this folder — do not delete or move it afterwards.

---

## 2. Get the template and configure it

In another directory where you plan to keep your coursework for this class:

```sh
git clone https://github.com/CS3704-VT/agent-template
cd agent-template
baker bake .
```

This installs the agent template, **opunit**, and **opencode**, and installs the git pre-commit hook.

---

## 3. Verify

```sh
baker check CS3704-VT/profile:agent-template.yml   # check your machine
```

Note any ✖ or ⚠️ and move on — do not try to fix them yourself today.

---

## 4. Start working

```sh
baker run setup      # prints what to do next
opencode
```

Inside OpenCode:

1. `@assignment analyze Project0` to pull in the assignment details. If this does not work, try providing the link to this file with `@assignment analyze <link>`
2. `/skills` -> learning-goal. Complete the learning goal-setting exercise for the semester (e.g., what you hope to get out of this course)
3. `<tab>` to switch between `plan` and `build`
4. `@dcbrown quiz me on the software development lifecycle`

---

## 5. Commit

Use the `Plan` and `Build` agents to plan and write some code (whatever you want is fine).

**Commit the code**
```sh
git add -A
git commit -m "Assignment 0"
```

Note whether the pre-commit hook did anything.

**Submit the assignment**
```sh
@assignment validate    # should verify if your work meets submission criteria
@assignment submit      # should package your work for submission, may fail if criteria are not met
```

---

## 6. Tear it down

```sh
baker cleanup --dry-run    # shows what would be removed, changes nothing
baker cleanup              # answer the prompts (answer No for now)
```

**Do not run the full cleanup for today's test!** You will keep this environment until the end of the semester. If you would like to uninstall all configurations at the end of the class, use `baker cleanup` instead of `baker bake` on all of the baker.yml files for projects and assignments. You will need to uninstall Baker and all of the prerequisite programs on your own if you wish to remove them.

---
### Submit

Submit a document on Canvas with the following items:

For each step, share whether the task passed or failed. Please provide the exact error if it failed.

1. Node + git present, ARC key persisted
2. Baker installed
3. `baker bake .`
4. `baker check` (pre-bake and post-bake checks pass)
5. `baker run setup`
6. OpenCode started, `@assignment analyze` collected correct details
7. `/learning-goal` completed
8. Commit + hook (`learning-opportunity` skill triggered)
9. `baker cleanup`

Also please answer the following questions: 
* What was confusing?
* Was there any step where you were unsure what to do, or what had just happened?
* Add your learning goal responses (or upload a separate file)
* Add your machine details, including **Your OS and versions** (macOS / Windows / Linux (provide distro) and `node --version`, `npm --version`)

