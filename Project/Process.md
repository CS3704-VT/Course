# Process

### __Lightning Talk__ (15%)
Your group must complete an oral proposal presentation during class provding an overview of the project you wish to complete for the semester. This talk must include a problem statement, your proposed solution, how your proposed work relates to the overall project goal, and **at least one** example `requirement` use cases (see below for details). You may divide the presenting duties among your team however you wish, but the talk must be **_no more than 5 minutes_**. There will also be a brief time of Q&A from students after each presentation on your proposed work.

   **Rubric: TBD**

#### __Use Case__

A use case is a way to describe a task that a user wants to perform and the required sequence of steps needed to accomplish that task. It also includes possible error states. For more information about use cases, see slides.

In your lightning talk, you must present at least one formal use case that describes a requirement for the primary functionality of your system from a user's perspective.

For instance, this is an example use case for a bot to automatically schedule a meeting between developers:

```
Use Case: Create a meeting
1 Preconditions
   User must have google calendar api tokens in system.
2 Main Flow
   User will request meeting and provide list of attendees [S1]. Bot will provide  possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
  [S1] User provides /meeting command with @username,@username list.
  [S2] Bot will return list of meeting times. User will confirm time.
  [S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
  [E1] No team members are available.
```

### Project Proposal (15%)

Your project team must also submit a project proposal document. The proposal must conform to the International Conference on Software Engineering (ICSE) formatting guidelines (see the [MS Word](https://www.acm.org/binaries/content/assets/publications/word_style/interim-template-style/interim-layout.docx), [Latex](https://www.acm.org/binaries/content/assets/publications/consolidated-tex-template/acmart-primary.zip), and [Overleaf](https://www.overleaf.com/gallery/tagged/acm-official#.WOuOk2e1taQ) templates). The proposal must introduce your project and provide a high-level overview of the SE process your team plans to use. Your document should be no more than 2-pages (excluding references). Please check your document for typos and spelling or grammar errors. The proposal must contain:

* a relevant _title_ and all group members listed as _authors_;
* an _abstract_ briefly describing the problem and proposed solution;
* an _introduction_ that further explains the problem and motivates the need for the proposed solution;
* _related work_ presenting relevant software engineering tools or research studies; 
* a brief description of the _software engineering process_ your team plans to use for the project and why;
* and _references_ to any appropriate citations, if applicable. 

 * You will receive feedback from the teaching staff on the document and presentation for your proposal to approve of your course project for the semester.

    **Rubric: TBD**

 **Due:** September 22 at 11:59pm
- [ ] Lightning talk slides
- [ ] Proposal document
