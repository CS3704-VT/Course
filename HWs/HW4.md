# HW4

This homework focuses on testing, human aspects of software engineering, and evidence-based software engineering, in addition to another hands-on contribution to a codebase. This assignment has three parts: (1) reading from the course textbook, [Evidence-based Software Engineering](../resources/ESEUR.pdf); (2) an open-source contribution in which you find an issue, learn a project's contribution norms, and fix the selected issue; and (3) a final reflection on the activity and the overall course. All work is individual and any meaningful AI use must be disclosed per the [course AI policy](../AI_POLICY.md).

## Part 1: Reading Assignment

Read the following from ESEUR (page numbers refer to the book's printed page numbers):

**Chapter 13: Experiments** — read the entire chapter (pp. 357-376).
- Focus on: measurement uncertainty, experiment design, benchmarking pitfalls, and survey pitfalls.

**Chapter 6: Reliability** — read the following sections:
- §6.6 Checking for intended behavior, introduction (pp. 168-169)
- §6.6.2 Testing (pp. 170-175), including §6.6.2.3 Estimating test effectiveness
- §6.6.3 Cost of testing (pp. 175-176)

Skim (recommended, not required): §8.3 Communicating a story (pp. 224-231) on presenting data honestly.

**Chapter 2: Human cognition** — read the following sections:
- §2.2.1 Built-in behaviors (pp. 24-25)
- §2.2.2 Cognitive effort (pp. 25-26)
- §2.2.3 Attention (pp. 26-27)
- §2.4.1 Short-term memory (pp. 30-33)
- §2.4.3 Recognition and recall (pp. 33-34)
- §2.5.1 Belief (pp. 38-39)
- §2.5.2 Expertise (pp. 39-41)
- §2.8.1 Personality & intelligence (pp. 52-53)
- §2.8.5 Overconfidence (pp. 55-56)
- §2.8.7 Developer performance (pp. 56-58)

**Chapter 3: Cognitive capitalism** — read the following sections:
- §3.4 Group dynamics, introduction (pp. 72-73)
- §3.4.4 Social learning (pp. 75-76)
- §3.4.5 Group learning and forgetting (pp. 76-77)
- §3.4.6 Information asymmetry (pp. 77-78)

**Chapter 5: Projects** — read the following sections:
- §5.5 Development teams (pp. 140-143), including §5.5.1 New staff and §5.5.2 Ongoing staffing

Skim (recommended, not required): §2.8.3 Decision-making (pp. 53-55) and §3.4.2 Motivating members (p. 74).

### Reading Questions

**TODO:** Answer each of the following in a short written response (roughly 150-200 words each). These are reflection questions mostly graded on your understanding of the reading and a thoughtful response, not on correctness.

1. **Measurement and benchmarks.** The reading describes how measurements shift depending on who or what does the measuring (developers' self-reported times vs. observers, tools that disagree with each other) and how benchmarks can be gamed or cherry-picked (Intel's "independent" Pentium 4 benchmarks, Samsung detecting benchmark apps, etc.). AI coding tools are now routinely marketed with benchmark scores. Discuss how a developer should evaluate AI-generated code or a claim that _"Tool X solves 70% of benchmark Y"_ or _"X is 2x faster than Y"_. What specific questions would be good to ask when you encounter numbers like this?

2. **Testing.** Section 6.6.2 notes that while test *inputs* can be generated automatically, "in only a few cases is it possible to automatically predict the expected output from the input" (the *test oracle* problem), that tests can contain mistakes just like source code, and that statement coverage is an imperfect measure of how many mistakes a test suite will detect (compare coverage to mutants killed, see Figure 6.54). What do these findings imply about using AI tools to generate test suites? If an AI tool tells you "I added tests and coverage is now 95%," what would you check before trusting that the code is well tested?

3. **Cognitive load and code comprehension.** Chapter 2 describes cognitive effort as a cost/accuracy trade-off, attention as a limited resource, and working memory as small and easily disrupted. It also shows that experts chunk and recall code differently from novices (the Adelson and McKeithen studies) and that people remember structured material better than scrambled material. Using these findings and your experiences, explain why reading and reviewing an unfamiliar codebase is hard and how AI might help or hurt. Then imagine your first months on a software team. You're handed a codebase you've never seen and asked to review a teammate's change. What are two things you would do to make this review easier? At least one must be something discussed in class.

4. **Measurement uncertainty.**  A simpler form of Goodhart's Law (13.1.1) states "When a measure becomes a target, it ceases to be a good measure". What does this suggest about using metrics like lines of code, commit counts, or PR counts for assessing productivity? What should you infer from claims about "10x developers" or lines of code/commit/PR counts? 

5. **Team cognition, group learning, and open-source norms.** The reading discusses shared mental models, communication overhead and peak team size, group learning and forgetting, information asymmetry, and social learning. Explain why onboarding, documentation, contribution guidelines, and public communication matter in a software team or open-source project.

## Part 2: 2026 Stack Overflow Developer Survey

Read the the [2026 Developer Survey results](https://survey.stackoverflow.co/2026) and the [Stack Overflow blog post](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) announcing the results. Then, answer the following reflection questions: 

6. Which result did you find the most interesting, and why? 

7. Which result did you find the most surprising, and why? 

8. Stack Overflow is a question-and-answer website where programmers ask and answer technical questions, from debugging an error message to choosing between design approaches. Launched in 2008, it became one of the most widely used resources in software development. However, Stack Overflow's traffic has declined as developers increasingly turn to AI tools for answers. What is your experience with Stack Overflow, and what does this shift mean for how software engineers learn, share knowledge, and build expertise?

9. **Surveys.** The reading suggests self-assessed skills only weakly correlate with actual performance, and thus survey-based claims should not always be trusted. What would you want to know about how this Stack Overflow survey was designed and analyzed before you relied on its results?

## Part 3: Capstone Reflection

**TODO:** Complete the following reflction of the course this semester:

10. Reflect on the [What Makes A Great Software Engineer](https://ieeexplore.ieee.org/document/7194618) paper discussd in the very first class. Which three traits or practices highlighted in the paper do you consider most essential for your future career, and why?

11. How do you think the attibutes of a great software engineer have/will change in the age of generative AI (be specific, using examples from the research paper)? How can SE courses (like this one) be better designed and structured to help students become great software engineers?

12. Throughout the semester we've revisited the quote by Dr. Anthony Bryant "[‘It’s Engineering... but not as we know it’… Software Engineering - solution to the software crisis, or part of the problem?](https://dl.acm.org/doi/epdf/10.1145/337180.337191)". Recently, structured software engineering processes are sometimes criticized for being too rigid and impeding AI-driven development progress. Based on this paper, do you believe software development processes are incompatible with the future of software dvelopment. Discuss using relevant examples and concepts from class, the paper, as well as your own experiences, to support your argument.

-----------

## Part 4: Open-Source Contribution (Extra Credit)

In HW3, you contributed to a course repository. In this part, you will find a real, active open-source project---which can demonstrate desireable skills for hiring managers (see [The Open Source Resume: How Open Source Contributions Help Students Demonstrate Alignment with Employer Needs](https://arxiv.org/abs/2510.25180)). For this activity, you will choose a beginner-friendly issue that you did not create, learn how the project expects contributions to be made, and fix the issue in your own fork. This part is optional, and will count as extra credit towards your final grade if all tasks are completed.

### 1. Find and justify a project and issue

**TODO:** Choose a real, public, active open-source project and an open issue that you did **not** create. The issue should be suitable for a new contributor (for example, labeled `good first issue`, `help wanted`, or `beginner`) and should ask for a bug fix, a small feature, a test improvement, or a documentation fix. Do not use a course repository, your own repository, or your Project 1/Project 2 repository. Choose your project early so you have time to set it up and make the change.

Use these resources to find candidates:

- [Good First Issue](https://goodfirstissue.dev/) and [Up For Grabs](https://up-for-grabs.net/)
- GitHub's [good-first-issue topic](https://github.com/topics/good-first-issue) and [issue search for `good first issue`](https://github.com/search?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22&type=issues) or `help wanted`
- [Awesome for Beginners](https://github.com/MunGell/awesome-for-beginners), [CodeTriage](https://www.codetriage.com/), and [Open Source Guides: How to Contribute](https://opensource.guide/how-to-contribute/)
- [First Contributions](https://github.com/firstcontributions/first-contributions) if you want to practice the GitHub fork/branch/PR workflow first
- Civic tech and humanitarian projects: [Code for America Brigade](https://brigade.codeforamerica.org/), [Hack for LA](https://www.hackforla.org/), [Code for Boston](https://www.codeforboston.org/), [Chi Hack Night](https://chihacknight.org/), [Ushahidi](https://github.com/ushahidi/platform), [Sahana Eden](https://github.com/sahana/eden), [OpenMRS](https://github.com/openmrs/openmrs-core), [DHIS2](https://github.com/dhis2/dhis2-core), [HOT Tasking Manager](https://github.com/hotosm/tasking-manager), and [Public Lab](https://github.com/publiclab/plots2)
- GitHub topics: [`humanitarian`](https://github.com/topics/humanitarian), [`civic-tech`](https://github.com/topics/civic-tech), [`hfoss`](https://github.com/topics/hfoss), and [`social-impact`](https://github.com/topics/social-impact)

These are starting points, not endorsements. Check that the project is active (recent commits, merged PRs, and issue responses), has an open-source license, and has a contribution process you can follow. Avoid issues that are assigned or already claimed, security-sensitive, very large, or dependent on hardware or private accounts you do not have.

In a short brief, include:

- Project name, URL, license, and primary language
- Issue number and URL, and a one-sentence summary of what it asks for
- Why you selected this project and issue (personal interest, humanitarian/civic relevance, skills you want to build, etc.)
- Evidence that the project is active and welcoming (recent activity, maintainer responses, labels, `CONTRIBUTING`/code of conduct)
- What you expect the change to involve, how you will verify it, and the main risks or unknowns
- **AI-use report:** Does the project have an AI contribution policy? If so, summarize it. How could AI appropriately help with this issue (for example, exploring the codebase, reproducing the bug, drafting tests, or editing documentation), what would you not delegate to AI, and what disclosure does the project require? If the project has no policy, say so and apply the course AI policy.

### 2. Contribution policy and engagement expectations

Before you start, read the project's `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and any AI-use policy. If the project's rules conflict with the course AI policy, follow the stricter project rule for the contribution itself, and disclose how you used AI for your own preparation.

**TODO:** Summarize the project's contribution documentation and AI policy.

### 3. Fork, reproduce, fix, and verify

**TODO:** Fork the repository to your GitHub account, clone your fork, add the original repository as an `upstream` remote, and create a branch for your change (for example, `fix/<issue-number>` or the name required by the project). Reproduce the bug or confirm the missing behavior before changing code. Then make the smallest correct change that addresses the issue, add or update tests when the project expects them, and run the project's build, tests, lint, and formatting checks.

Push your change to your fork and provide:

- A link to your fork and branch
- The commit hash or link to the commit(s)
- A short diff summary and an explanation of the change
- The commands you ran and the output showing that the build/tests/lint pass
- Before/after evidence (a failing test, a log, a screenshot, or a small script) when applicable
- Your AI-use disclosure: what you used AI for, what you changed or rejected, and how you verified the final result

The change must be substantive: a bug fix, a test improvement, a small feature, or a documentation fix that resolves the issue. A cosmetic-only change is acceptable only when the issue itself is cosmetic. Do not commit secrets, credentials, generated build output, large binaries, or unrelated reformatting. If the issue has already been fixed upstream, document that and choose another issue. If you cannot reproduce or fix the issue after a reasonable attempt, document what you tried and why you stopped, then choose a different issue rather than submitting an unverified change.

### 4. Open a pull request

_Optional bonus:_ Open a pull request from your fork to the original repository. The PR must follow the project's template and conventions, reference the issue (for example, `Closes #<issue>`), summarize the change, include your test evidence and AI-use disclosure if required, and respond professionally to review. A well-formed PR earns bonus credit even if maintainers do not merge it; merging is outside your control and is not required. Do not open a PR if the project's policies prohibit unsolicited or AI-assisted contributions, or if the issue is already claimed. Never pressure maintainers to review or merge; if there is no response after at least a week, a single polite follow-up in the same thread is appropriate.

### 5. [Reflection]

In a short paragraph (~150-200 words), reflect on Part 2. How did you find your project and issue, and what surprised you about the project's norms, documentation, or communication? What was harder than you expected: setting up the project, reproducing the issue, understanding the code, or keeping the change small? How did you verify your fix and any AI-generated suggestions? Which ideas from the human-aspects readings (for example, information asymmetry, group learning and forgetting, expertise, or cognitive load) help explain what you observed? Would you contribute to this project again, and what would you do differently next time? If you opened a bonus PR, describe how the review or lack of response affected your view of open-source contribution.


---

### Submit

Upload the following on Canvas:

- [ ] Your responses to questions 1-12
- [ ] Optional: Your open-source contribution question responses (rationale for project and issue selection, overview of contribution policy, and reflection)
- [ ] Optional: Links to your selected project and issue, your fork and branch/commit(s), and your pull request

**Due:** Friday (12/4) at 11:59pm
