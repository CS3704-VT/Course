# HW3

This homework focuses on implementation and maintenance in the SDLC. The assignment has three parts: (1) reading from the course textbook, [Evidence-based Software Engineering](../resources/ESEUR.pdf) (ESEUR); (2) an exploration of code review processes; and (3) a hands-on practical contribution to a coding project.

All work must be completed individually. You may use AI tools per the [course AI policy](../AI_POLICY.md). Any meaningful AI use must be disclosed, and your answers must demonstrate your own understanding.

## Part 1: Reading Assignment

Read the following from ESEUR (page numbers refer to the book's printed page numbers):

**Chapter 5: Projects** — read the following sections:
- §5.4.6 Implementation (p. 137)
- §5.4.8 Refactoring (p. 138)
- §5.6 Post-delivery updates (pp. 143-146), including §5.6.1 Database evolution

**Chapter 7: Source code** — read the following sections:
- §7.1 Introduction (pp. 177-182)
- §7.2 Desirable characteristics (pp. 183-198)
- §7.4 Evolution of source code (pp. 210-212)

Skim (recommended): §7.3 Patterns of use

### Questions

**TODO:** Answer each of the following in a short written response.

1. **Post-delivery updates.** The reading notes that long-lived systems keep changing. Summarize the main reasons maintenance never really ends for software projects, and provide one concrete maintenance or data-evolution strategy. Why does this make "done" a fiction for most software?

2. **Reading code.** Chapter 7 suggests that reading code is a distinct, effortful activity shaped by identifier names, narrative structure, and limited working memory. What does this imply for how you write code and tests that others (including your reviewer) must understand?


## Part 2: Code Reviews

3. [Reflection] What is your personal experience with code reviews? Discuss practices, guidelines, tools, etc. used from your perspective as a reviewer giving feedback on someone else's code and a programmer receiving feedback on your own code. If you do not have code reviewing experience, explain how you would accomplish the above tasks in a professional setting.

4. Many software engineering teams provide checklists or guidelines for developers to be efficient and effective in code reviews (which research shows improves the overall review process and code quality, see [[McIntosh, 2015]](https://link.springer.com/article/10.1007/s10664-015-9381-9)). Visit Awesome Code Review's [Company Specific Code Review Practices](https://www.awesomecodereviews.com/companies/company-specific-code-review-practices/) guidelines for software teams at prominent tech companies. Select code review guidelines for two different companies, providing a brief rationale for those choices. What concepts are similar between the companies (List at least two)? What are some key differences (List at least two)?

For the following activities, you will review code reviews on the Code Review Stack Exchange (https://codereview.stackexchange.com/) website, a Stack Overflow-like website for code reviews between peers online. To analyze reviews, you may use either of the code review guidelines from above, another code review checklist online (cite the source), or your own personal knowledge, opinions, and experience.

5. Find an example of a "good" code review. Provide a link to the review and explain why you found the review beneficial.

6. Find an example of a "bad" code review. Provide a link to the review and briefly explain why you found the review not beneficial. In addition, include recommendations for improvement to the review feedback.

## Part 3: OpenLeetcode Contribution

For the final activity, you will extend an existing codebase using a typical contribution workflow. The repository will be [CS3704-VT/OpenLeetcode](https://github.com/CS3704-VT/OpenLeetcode), a course fork of an open-source version of [LeetCode](https://github.com/mbucko/openleetcode). You will complete the full contribution cycle on the shared course repository. 

Review the repo `README.md`, then follow the existing [`data/problems/TwoSum/`](https://github.com/CS3704-VT/OpenLeetcode/tree/main/data/problems/TwoSum) example as a guide for the project directory layout, file naming, solution format, and `.test` test case format exactly. In short, each problem lives under `data/problems/<ProblemName>/` with a problem statement (`description.md`), solution files in the target language (`solution.cpp`/`solution.py` and `solution_expected.*`), and test cases (`testcases/TestCaseN.test`). For your convenience, the course agent-template skills and agents and an orientation file have already been provided if you choose to use them.

7. Create an issue

**TODO:** Create a GitHub issue proposing one [common LeetCode problem](https://leetcode.com/discuss/post/460599/blind-75-leetcode-questions-by-krishnade-9xev/) that is *not* already in the repo (existing: `TwoSum`, `LongestSubstringWithoutRepeatingCharacters`, `NumberOfIslands`, `CheckCompletenessOfABinaryTree`) or submitted as an issue. Use the name of the problem as the title and create an issue with `problem` issue template and include:
- [ ] Problem name/title and a link to the LeetCode problem
- [ ] Difficulty
- [ ] Target language (C++ or Python)
- [ ] A functional description, input/output format, and constraints
- [ ] At least one test case (inputs and expected outputs)

> :warning: Please create your issue early so other students have something to contribute to for this assignment!

8. Implement another student's issue

**TODO:** Claim an open issue from a **different** student and implement it on a branch (e.g., `problem/<name>`), adding the problem directory and files above. Issues are claimed **first-come**. Implement the solution to your selected problem, then build and run the CLI to prove your reference solution passes every test case:

```sh
./install.sh --prefix=./install
cd install/OpenLeetCode
./openleetcode.sh --language <cpp|python> --problem <ProblemName> --testcase All --verbose
```

After your testing is complete, open a pull request to `CS3704-VT/OpenLeetcode` that references the issue (e.g., `Closes #<issue>`). Include a summary of the change, the CLI test results, and your AI-use disclosure.

9. Peer review (assigned)

**TODO:** Review **another** student's open pull request (not your own created issue or your own PR) and post a review comment covering:
- [ ] **Overview** — a short summary of the review
- [ ] **Correctness** — does it solve the problem and pass all test cases?
- [ ] **Complexity** — time and space complexity; is it reasonable and explained?
- [ ] **Quality** — readability, naming, and adherence to repo conventions
- [ ] **AI-specific concerns** — if AI was used, what issues were found and what was learned
- [ ] **Recommendation** — approve, return for changes, etc.

When the submission is appropriate, merge it into the codebase. Then respond to the review on your own PR and reconcile any requested changes from the review.

10. [Reflection] Reflect on your experience for Part 3 of the homework. Have you completed this process before? What is your experience with contributing to collaborative software projects using GitHub? Did you use AI, and was it helpful or harmful for this process?

---

### Submit

Upload the following on [Canvas](https://canvas.vt.edu/courses/234343/assignments/2839424):
- [ ] A single PDF containing your responses to questions 1-6 and your Part 3 reflection (question 10)
- [ ] Links to your issue, your pull request, and your review comment (questions 7, 8, and 9)

Other grading checks:
- [ ] Your issue, PR, and review will be verified on GitHub

**Due:** Friday (10/30) at 11:59pm
