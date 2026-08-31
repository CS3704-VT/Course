# HW1

This homework covers the first unit of the course: what software engineering is, the software development lifecycle (SDLC), and the process models teams use to move through it. It has three parts: (1) a reading from the course textbook, [Evidence-based Software Engineering](../resources/ESEUR.pdf); (2) questions on software process models; and (3) a short research task on the processes companies actually use in practice. All work is individual. You may use AI tools other than Opencode, but must adhere to the [course AI policy](../AI_POLICY.md): **any meaningful AI use must be disclosed!** Please upload your answers to the questions on the [Canvas assignment](https://canvas.vt.edu/courses/234343/assignments/2839422) as a .pdf file or provide your responses in the text entry form. You are primarily graded on how you demonstrate your understanding of the material and justify your responses.

## Part 1: Reading Assignment

Read the following pages from the textbook:

**Chapter 1: Introduction** — read the following sections:
- §1 Introduction (pp. 1-2)
- §1.2 Software Markets (pp. 5-8)
- §1.4 Overview of Contents (pp. 12-14) [overview of entire textbook]

**Chapter 4: Ecosystems** — read the following sections:
- §4.1 Introduction (pp. 91-93)
- §4.4 Organizations (pp. 104-109)
- §4.5 Applications and Platforms (pp. 109-112)
- §4.6 Software Development (pp. 112-118)

**Chapter 5: Projects** — read the following sections:
- §5.3 Resource Estimation (pp. 125-130)
- §5.4 Paths to delivery (pp. 130-131)
- §5.4.1 Development methodologies (pp. 131-132)
- §5.4.2 The Waterfall/iterative approach (pp. 132-133)
- §5.4.3 The Agile approach (p. 133)
- §5.4.4 Managing Process (pp. 133-135)


Optional: Skim (recommended, not required) §5.1 Introduction (pp. 119-122) on project culture, lifespan, and cancellation rates.

### Reading Questions

**TODO:** Answer each of the following in a short written response (1-3 sentences each). These are reflection questions mostly graded based on your understanding of the reading and a thoughtful response, not evaluated based on correctness.

1. **Software Engineering.** The textbook opens by calling software engineering a "_craft activity_" that people learn by making their own mistakes, and suggests this practice survived because for 60+ years customers paid whatever it cost and waited however long it took for software (a "sellers market"). In your own words, explain what this means. Then reflect on your own experience: when you learned to code or took other programming classes (e.g., CS2114, etc.), did you find yourself learning more by trial-and-error (craft) or by applying established principles (engineering)? Give one specific example. Finally, consider the current age of AI-assisted software engineering (tools like Claude Code, GitHub Copilot, or the AI tools we will use in this class). Does AI make software development more like a craft or more like an engineering discipline? Explain your reasoning (there is no correct answer).

2. **Software Development Lifecycle.**  Chapter 4 argues that software ecosystems are driven by customer demand rather than physical deterioration (hardware). For instance, software does not wear out, but the world around it changes. Based on this and given what the reading says about how effort is distributed across SDLC phases, which phase of the SDLC do you feel is most important, and why? Which phase is most interesting to you personally? Please give specific examples

## Part 2: Software Process Models

**TODO:** Answer each of the following.

3. From the software engineering processes discussed in class, select which one would be the best in the scenarios below. To get full credit, you must answer with a **unique** process for each scenario (i.e., only use waterfall for one response) and provide a reasonable justification for why you selected that specific process:

   a) You are developing a software application for a space mission to the moon in the 1970s.

   b) You are developing an open-source word processing application in the 1990s.

   c) You are working with other students in CS3704 on the team project for this class.

   d) Your client keeps requesting to remove several high-priority features added to the product.

   e) You are developing a software application for a space mission to the moon in 2030.

4. In your own words, describe the difference between plan-driven and iterative process models. What are the advantages of iterative models over plan-driven processes? What are the advantages of plan-driven models? Waterfall was originally designed as a plan-driven approach where work on each phase does not start until the previous phase is complete. However, Figure 5.30 shows that various software development efforts (Design, Coding, Integration, Acceptance Testing) actually occurred across phases using Waterfll in practice. What does this suggest about plan-driven development on paper vs. how projects are really run in the real world? 

5. A software developer on your team is spending too much time working on unrelated tasks. What is one agile or project management practice that would help? How?

6. The Chaos software development model, created by someone only known as L. B. S. Racoon, is based on strategies for the two-person games Chess and Go and is defined in it's simplest form as "always resolve the most important issue first". Skim [The Chaos Model and the Chaos Cycle](https://dl.acm.org/doi/10.1145/225907.225914) (follow-up article [here](https://timross.wordpress.com/wp-content/uploads/2019/06/stratx23.pdf)) and briefly describe the advantages and disadvantages of this model based what you know about software processes.


## Part 3: Software Processes in Practice

The goal of this task is to understand what software engineering processes companies actually use in practice.

**TODO:** Search online to find software development process models used by **at least three companies**:
- one FAANG or FAANG-adjacent large tech company,
- one smaller organization, and
- one firm (any size) that you would like to work for someday.

Search for documentation on the specific SE processes used by software engineers at that company (i.e., blogs, technical reports, case studies, articles, research papers, etc.). Add the following information to the shared [class spreadsheet](https://docs.google.com/spreadsheets/d/1mLqDDqADDcx7bs7XYnrB2-gNAJLmIN1Nyc_W-_TORr0/edit?usp=sharing):

- [ ] Your name/PID
- [ ] Company name
- [ ] SE process used
- [ ] Link to resource
- [ ] Any company-specific details on process implementation (if applicable)
- [ ] Reported challenges (if applicable)
- [ ] Benefits (if applicable)

Then briefly review your entries in the context of other responses on the spreadsheet to answer the following. Questions 8 and 9 should be a few sentences each; question 10 should be a solid paragraph.

7. After reviewing the class spreadsheet, which software development processes appear to be the most commonly used? Are there any patterns you noticed across companies? What was the most interesting or surprising thing you noticed in the list?

8. The textbook notes Waterfall was originally designed as a risky sequential approach, yet it was highly adopted as a standard development technique and "_continues to haunt software project management, despite repeated exorcisims over several decades._" (p. 131). In addition, Chapter 5 notes there is a lack of measurement data on Agile development processes ("_The rarity of measurement data for any of the agile processes means this evidence-based book has little to say about them_", p. 133). Why is this a problem, and what does this suggest about how development practices actually get adopted? What kinds of evidence would you look for to demonstrate a software development process (waterfall, agile, or other) is improving how developers build software day-to-day?

9. The textbook describes development methodologies as providing "_management support for necessary fictions_" (p. 131) to create an image of control for clients even when the actual process is messier. Based on the reading, the class spreadsheet, and your own knowledge/experiences, are software process models necessary for modern software development? Why or why not?

---
### Submit

Upload the following on [Canvas](https://canvas.vt.edu/courses/234343/assignments/2839422):
- [ ] A single PDF or text entry response containing your responses to questions 1-9

Other grading checks:
- [ ] Your three company entries will be checked on the shared class spreadsheet
- [ ] Responses must be your own writing; disclose any meaningful AI use per the [AI policy](../AI_POLICY.md)

**Due:** Friday (9/11) at 11:59pm
