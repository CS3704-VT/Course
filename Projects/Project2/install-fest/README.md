# CS3704 Project 2 — Environment Setup

This repository holds one `baker.yml` per Project 2 codebase. Each one does two things to your fork of the project:

1. **Installs what the project needs:** git, Node.js, opencode, and anything project-specific (Python, Flask, etc...).
2. **Adds the course agents and skills** from the course [agent-template](https://github.com/CS3704-VT/agent-template).


Follow **[Option A](#option-a--set-up-with-baker-recommended)** for instructions with Baker. If you were not able to get Baker working on your machine, use **[Option B](#option-b--manual-setup-no-baker)**.


## Find your project

| Project | Original repository | Folder in this repo |
|---------|---------------------|---------------------|
| Art Reference Archive | [Affelis/Art-Reference-Archive-CS3704-pr1-](https://github.com/Affelis/Art-Reference-Archive-CS3704-pr1-) | [`art-reference-archive/`](art-reference-archive/baker.yml) |
| Hokie Scheduler | [VTgrace/CS3704_Project1](https://github.com/VTgrace/CS3704_Project1) | [`hokie-scheduler/`](hokie-scheduler/baker.yml) |
| Skynet Internship Finder | [rcolinmichaelvt/Skynet](https://github.com/rcolinmichaelvt/Skynet) | [`skynet/`](skynet/baker.yml) |
| StudyTime | [CKepperling/StudyTime](https://github.com/CKepperling/StudyTime) | [`study-time/`](study-time/baker.yml) |
| The Clubhouse | [sania-jain/The-Clubhouse](https://github.com/sania-jain/The-Clubhouse) | [`vt-risk/`](vt-risk/baker.yml) |
| Hokie Trade | [nati2405/Hokie_Trade](https://github.com/nati2405/Hokie_Trade) | [`hokie-trade/`](hokie-trade/baker.yml) |

In the commands below, replace:

- `<original-owner>/<project-repo>` with the **Original repository** of your project
- `<forked-username>` with the GitHub username for your forked repo
- `<folder>` with your project's **Folder in this repo**


---

## Step 0 — Pre-requisites

Opencode and your ARC API key should be setup from the [Project 0](https://github.com/CS3704-VT/Course/blob/main/Projects/Project0/PM0.0.md) assignment.

### Node version

Most of these projects will not install on an old Node.js:

| Project | Needs Node |
|---------|-----------|
| VT Risk | **22 or newer** |
| Hokie Scheduler, StudyTime, Hokie Trade | 20.19+ or **22.12+** |
| Skynet, Art Reference Archive | 18 or newer |

If `node --version` is lower than your project needs, install the appropriate version from [nodejs.org](https://nodejs.org) (or use `nvm`).

---

## Step 1 — Fork and clone your project (One Project 2 team member)

1. One team member needs to open your project's **original repository** on GitHub and click **Fork** (top right). 
2. Clone **the forked repository**, not the original, and `cd` into it:

   ```bash
   git clone https://github.com/<forked-username>/<project-repo>
   cd <project-repo>
   ```
---

## Option A — Set up with Baker (recommended)


### A1. Download your project's baker file

From the top level of your fork:

```bash
curl -o baker.yml https://raw.githubusercontent.com/OWNER/REPO/main/<folder>/baker.yml
```

> **Windows PowerShell:** type `curl.exe`, not `curl`. In PowerShell, plain `curl` is a different command and the line above will fail.

Example for Skynet:

```bash
cd Skynet
curl -o baker.yml https://raw.githubusercontent.com/OWNER/REPO/main/skynet/baker.yml
```

### A2. Bake

```bash
baker bake .
baker run setup
```

- `baker bake .` installs the tools and adds the agents, skills, and git hook to your fork.
- ⚠️ **_If one student is able to make it here, then they can push these changes to GitHub and everyone else should be able to pull and get the agent-template setup! Additional dependencies will have to be added manually though..._**
- `baker run setup` installs your project's own dependencies (`npm install`, and so on) and prints what to do next. It must run **after** `bake`, from the same folder.

---

## Option B — Manual setup (no Baker)

Use this if Baker would not install or `baker bake` keeps failing. You will do by hand exactly what the baker file does.

> **Windows:** run every command in this section in **Git Bash**, **not** PowerShell or Command Prompt.

### B1. Get agent-template next to your project

Clone it into the folder that **contains** your fork, not inside your fork:

```bash
cd ..                                                    # leave your fork
git clone https://github.com/CS3704-VT/agent-template
cd <project-repo>                                        # back into your fork
```

You should now have two sibling folders, `agent-template/` and `<project-repo>/`.

### B2. Copy the agents, skills, and config into your fork

From the top level of your fork, paste this whole block:

```bash
T=../agent-template

# Agents, skills, plugin, helper scripts
mkdir -p .opencode
cp -R "$T/.opencode/." .opencode/

# Model provider config and the current phase list
cp "$T/opencode.json" "$T/PHASE.md" .

# Templates the agents use for requirements and design documents
mkdir -p docs/templates
cp "$T"/docs/templates/*.md docs/templates/

# Learning-opportunity git hook
cp "$T/hooks/post-commit" .git/hooks/post-commit
chmod +x .git/hooks/post-commit .opencode/scripts/*.sh

# Shared agent instructions: ADD to an existing AGENTS.md, never overwrite it
if [ -f AGENTS.md ]; then printf '\n' >> AGENTS.md; cat "$T/AGENTS.md" >> AGENTS.md
else cp "$T/AGENTS.md" .; fi

# Keep agent logs, generated goals, and opencode's runtime files out of git
printf '\n' >> .gitignore; cat "$T/.gitignore" >> .gitignore
```

Check that it worked:

```bash
ls .opencode/agents          # assignment.md  build.md  dcbrown.md  plan.md ...
ls .opencode/skills          # analysis  concept-explain  learning-goal  quiz ...
```

### B3. Install your project's dependencies

Run the block for **your** project from the top level of your fork (still in Git Bash on Windows).

**Art Reference Archive** (needs Python 3)

```bash
python -m pip install flask          # macOS/Linux: python3 -m pip install flask
```

**Hokie Scheduler**

```bash
cd hokie-scheduler
npm ci
npm run setup                        # creates hokie-scheduler/.env (API keys are optional)
cd ..
```

**Skynet**

```bash
npm install
```

**StudyTime** (needs [Docker Desktop](https://www.docker.com/products/docker-desktop) and
Python 3.12: `winget install Python.Python.3.12` on Windows)

```bash
cd backend
python -m venv .venv                 # macOS/Linux: python3.12 -m venv .venv
.venv/Scripts/pip install -r requirements.txt ruff     # macOS/Linux: .venv/bin/pip ...
cd ../frontend
npm ci
cd ..
```

StudyTime also needs a `.env` file at the top level. The README says to copy `.env.example`,
but that file is not in the repository, so get the values from the original team or
your instructor.

**The Clubhouse**

```bash
npm install
cp -n .env.example .env.local        # blank values = runs on mock data
```

**Hokie Trade** (also install **Expo Go** on your phone)

```bash
npm install
```

---

## Before you start working

### Commit the setup to your fork


### Start the agents

From the top level of your fork:

```bash
opencode
```

Then, inside opencode:

```
@assignment analyze PM2            # pulls the assignment details into your project
/skills  →  learning-goal          # set your goals for this project (10–15 minutes)
/skills  →  orient                 # to familiarize your team with the new codebase
```


The full guide is agent-template's
[STUDENT_GUIDE.md](https://github.com/CS3704-VT/agent-template/blob/main/docs/STUDENT_GUIDE.md).
