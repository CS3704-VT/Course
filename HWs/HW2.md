# HW2

This homework covers the requirements and design phases of the software development lifecycle (SDLC). This covers how teams discover, analyze, and specify what to build, and how they make design decisions that shape the code they will write. There are two parts: (1) a reading from the course textbook ([Evidence-based Software Engineering](../resources/ESEUR.pdf)) with reflection questions; and (2) questions and tasks that explore requirements and design, using AI tools from the course agent template to help generate the artifacts. All work is individual. You must use the assigned Opencode agent template for this assignment, and must adhere to the [course AI policy](../AI_POLICY.md). Please upload your answers on the [Canvas assignment](###) as a .pdf, .txt, or provide your responses in the text entry form. You are primarily graded on how you demonstrate your understanding of the material and justify your responses.

## Part 1: Reading Assignment

Read the following pages from the textbook. The textbook is organized around what has actually been measured, and there is considerably more evidence available on requirements than on design — so Part 1 focuses on requirements, and you will engage with design hands-on through the agent tasks in Part 2.

**Chapter 3: Cognitive capitalism** — read the following section:
- §3.4.6 Information asymmetry (pp. 77-78) 

**Chapter 5: Projects** — read the following sections:
- §5.2.1 Contracts (pp. 124-125) 
- §5.4.5 Discovering functionality needed for acceptance (pp. 135-136) 

**Chapter 6: Reliability** — read the following section:
- §6.4.1 Requirements (pp. 161-162) 

### Reading Questions

**TODO:** Answer each of the following in a short written response (1-3 sentences each). These are reflection questions mostly graded based on your understanding of the reading and a thoughtful response, not evaluated based on correctness.

1. **Requirements.** Chapter 6 suggests the number of mistakes found in requirements can be of the same order of magnitude as — or even exceed — the number of mistakes found in the code itself. The textbook (and lectures) note that requirements are often ambiguous, incomplete, or misinterpreted as a project proceeds, which leads to increased chances of project failure. What does this suggest about the importance of requirements and how much effort teams should invest up front in requirements? Finally, reflect on your own experience. Describe a time when the initial requirements of a system you worked on differed from what you actually built. Give one specific example.

2. **The information gap.** Chapter 3 describes _information asymmetry_, where building a substantial software system involves "a huge amount of project specific information" (i.e., the application domain, software development, etc.). However, different aspects of a project/team hold parts of this information that are difficult for others to obtain. As a result, "writing a sufficiently exact specification of what a software system is expected to do, along with tightly defined acceptance criteria is time-consuming and costly". Based on the reading and what we've discussed in class so far, what is your opinion on whether plan-driven requirements engineering or iterative requirements processes are better for resolving this challenge? Do you have experience with this information gap where you or another project stakeholder (e.g., manager, teammates, instructor, client, etc.) lacked critical information about the requirements for a software project? How did you resolve this issue?

## Part 2: Startup Requirements and Design with AI Agents

For the following questions, go to the following website to generate a random startup for your project: [https://tiffzhang.com/startup/](https://tiffzhang.com/startup/) (Clicking "Get Started" will automatically generate another random startup for you if you would like to change). It generates a startup name, a short description/tagline, and a one-page marketing template. Use the **name and description** as the seed for your work: write a 1-2 sentence pitch for the product in your own words, and identify the target users and stakeholders for the company. The generated web template is an optional visual reference — only share it with the `ux-ui-designer` in Part 2 if it helps establish the product's visual style. You have just been hired as the requirements analyst for this company. Please complete the following activities to analyze and specify requirements and design for the start-up organization.

**Using AI Agents.** For each question below, you will use agents from the course agent-template (`../agent-template`, phase2 branch) to generate the specified artifacts. Each question describes the artifact you should ask the agent to produce. You must include the **generated artifact output** in your submission — not just a summary. If you prefer not to use AI agents, you may generate the requirements and design artifacts manually and your responses will be graded on the same criteria (no agent-output reflections are necessary). Disclose any meaningful AI use per the [course AI policy](../AI_POLICY.md). The agents may ask clarifying questions or work incrementally, so you may need multiple messages/turns to produce a complete artifact (e.g., the `requirements-analyst` will not write requirements based on unconfirmed assumptions). Answer them, including the question-and-answer exchange in your submission, or explicitly instruct the agent to proceed by stating its own assumptions. All diagrams will be text-based (ASCII/mermaid-style); agents do not generate image files. If a later artifact (design, UI) depends on an earlier one (requirements, use cases, user stories), you should be able to annotate the connection so it is clear which requirement each element satisfies (e.g., `-> UC-003`, `-> US-2 acceptance criterion`, etc.).

**TODO:** Answer each of the following. For each question, include your initial prompt and the generated responses and output from the agents.

3. **Requirements Elicitation:** Provide the agent with your startup's name and a 1-2 sentence pitch. Instruct the `product-manager` agent to produce a stakeholder analysis, identifying at least three stakeholders and their roles, and requirements elicitation questions aimed at those stakeholders for eliciting requirements for this system. 

> Include your initial prompt, the generated output, and a brief reflection on the elicitation questions.

4. **Requirements Prioritization:** Using the stakeholder analysis and elicited requirements from question 3, instruct the `product-manager` agent to produce:
(1) a prioritized list of candidate features for the startup using a prioritization framework (e.g., MoSCoW Must/Should/Could/Won't scoring), with a brief rationale for the priorities; 
(2) a short product recommendation framed in terms of user value.

> Include your initial prompt and the generated output in your response. If necessary, update the prioritized requirements generated by the agent. Your priorities may inform the requirements and design other agents write in upcoming questions.


5. **Requirements Generation:** Instruct the `requirements-analyst` agent to generate structured requirements for your startup. It should produce: 
(1) at least three functional requirements and three non-functional requirements; 
(2) at least two use cases (textual format) with actors, preconditions, main flow, alternative flows, and postconditions; 
(3) at least two user stories in the standard format with acceptance criteria in Given/When/Then format.

> Include the prompt and all generated agent output (all structured requirements, user stories, use cases) in your response.

6. **Use Case Diagrams:** Based on the requirements you just generated, instruct the `requirements-analyst` agent to create a use case and/or sequence diagram showing all actors and use cases with system behavior details for each use case.

> Include the use case/sequence diagram and system behavior details for each use case in your response.

7. **High-Level Design:** With your startup context and generated requirements, instruct the `system-architect` agent to devise a high-level design plan for your startup. The system should produce: 
(1) rationale for a high-level architectural design pattern; 
(2) a text-based architecture diagram showing major components and ER digram outlining potential data flows; 
(3) a technology stack recommendation with rationale for each choice; 
(4) at least one Architecture Decision Record (ADR) with context, decision, alternatives considered, and consequences.

> Include the architecture diagram, ER diagram, technology stack with rationale, and at least one ADR in your response.

8. **Low-Level Design:** Pick one key component from your high-level design. Instruct the `system-architect` agent to recommend a low-level design pattern for that system component, then produce a class diagram showing key classes, attributes, and methods and, if applicable, a data model/schema for the component's necessary data. Following the traceability note above, tag each class with the use case or user story it supports. A design pattern is only "right" relative to its alternatives, so also:

   (a) propose a **second [plausible design pattern](https://refactoring.guru/design-patterns/catalog)** for the same component that was not recommended by the agent;
   (b) ask the `system-architect` agent to assess both options (e.g., *"you recommended `<X>`; I'm proposing `<Y>` as an alternative. Compare them honestly — when would `<Y>` be better, and where is `<X>` still superior?"*);
   (c) ask the agent to create a **comparison table** outlining the strengths, weaknesses, and impacts (e.g., maintainability, extensibility, testability, performance, complexity) of each candidate pattern;
   (d) based on the information provided, **make a final choice** (_you_, not the agent) for a final design pattern and why it wins given your hypothetical startup's specific constraints.

> Include in your submission the class diagram, data model/schema, the comparison table, and your final decision on the design.

9. **UI Design and Heuristic Review:** Instruct the `ux-ui-designer` agent to design a user interface for your startup system, providing a primary user flow (step-by-step interactions) for two of the main use cases and an explanation of how the design maps to the user stories. Link each screen to the user story or use case (and acceptance criterion) it supports. Then, use the `heuristics-nielsen` skill (or instruct `ux-ui-designer` to use it) to review the generated UI design based on Nielsen's 10 usability heuristics — for each heuristic, state whether the design satisfies it and identify at least one specific improvement if it does not.

> Include in your submission at least one user flow, wireframe descriptions for at least two screens, the mapping of design to user stories, and the Nielsen's heuristics review assessing all 10 heuristics.

10. **Reflection.** Reflect on the agent-based workflow for each requirements and design phase. What worked well? What limitations did you encounter? How did interacting with the agents change your understanding of requirements and design? What would you do differently next time? If you chose to work manually, explain why and how your process differed. 


---
### Submit

Upload the following on [Canvas](https://canvas.vt.edu/courses/234343/assignments/2839423):
- [ ] A single PDF or text entry response containing your responses to questions 1-10

Other grading checks:
- [ ] Responses must be your own writing; disclose any meaningful AI use per the [AI policy](../AI_POLICY.md)

**Due:** Wednesday (10/7) at 11:59pm
