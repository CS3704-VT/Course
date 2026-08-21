# HW0

This homework will help you with setup and preparation for the course this semester.

## Course Overview

**TODO:** Review the [course syllabus](../SYLLABUS.md).

- [ ] Based on the syllabus and first lecture, fill out this [syllabus survey](https://docs.google.com/forms/d/e/1FAIpQLSe21UdpR4YSbNzI1rKE9_5aa7WF_2NlBK0PLTorHGw2atlb4A/viewform?usp=sf_link) with any questions, confusions, or concerns you still have about the course this semester. **Even if you do not have questions about the course, you must still complete the survey to receive full credit!**

## Mattermost

The primary mode of communication for the course this semester will be [Mattermost]. Communication is essential in software engineering and the majority of development teams use some form of IM or messaging system. Mattermost is one example of these types of platforms, and we will use it in class to provide course updates, answer questions, form project groups, and other course activities. For your profile, please include set your Full Name to be your first and last name (or name you prefer to go by), your Username to be your VT PID, and your Email to be your VT email address. 

You may download the free version of the Mattermost desktop application at [https://mattermost.com/apps/](https://mattermost.com/apps/) or use it online from your preferred web browser [https://meet.cs.vt.edu/cs-3704](https://meet.cs.vt.edu/cs-3704). To sign up for the workspace for this course, visit the invite link [here](https://meet.cs.vt.edu/signup_user_complete/?id=srrb9ndtmf8ddkqyx96nsjthwr). This platform is hosted on a server through the CS department. If you have problems or are unable to join via the link, please contact the instructor.

### Introduction

**TODO:** To further help us get to know each other, please introduce yourself. Write a brief paragraph in the #Town Square channel of the CS5704 Mattermost that contains the following information:
- [ ] Name
- [ ] Where are you from?
- [ ] Do you have any previous software engineering experience? If so, where did you work and for how long?
- [ ] What do you hope to get out of this course?

## Software Configuration

For this course, you are required to install the following software on your system.

* [Git](https://git-scm.com/) is the version control system we will be using in this course for class activities and collaborating on your team project. You may download the git client to your system [here](https://git-scm.com/downloads). Additionally, you will need a [GitHub](https://github.com/) account. After installation, [configure git](https://git-scm.com/book/ms/v2/Getting-Started-First-Time-Git-Setup) with the email address associated with your GitHub account.
* [Docker](https://www.docker.com/) provides containerized environments to accelerate development and deployment of software systems. You will also need [Docker Compose](https://docs.docker.com/compose/) and the [Docker Labspaces extension](https://hub.docker.com/extensions/dockersamples/labspace-extension). Several workshops will leverage Docker Labspaces, including the in-class workshop on 9/1.
* [NodeJS](https://nodejs.org/en) is a JavaScript runtime environment. For this class, we will primarily use node for [npm](https://www.npmjs.com/), a package management system with the largest software registry of tools and services for developers.
* Baker is a tool to automatically configure and verify your machine is correctly setup for a course, workshop, or homework assignment. More details are available [here](https://github.com/chbrown13/Baker). You can install Baker using the following commands (requires npm install):

```bash
git clone https://github.com/chbrown13/Baker
cd Baker
npm install
npm link
baker --version    # verifies Baker installed
```

Additional software will be used in class throughout this semester, but Baker will be used to support installation for specific assignments, workshops, and projects. You may be asked to install additional software for class activities if an issue arises or you face problems with Baker.

**TODO:** Run the following command below to verify the configuration of your laptop for this course. Upload a screenshot of the resulting output. All checks should pass with green checks.

```baker check CS3704-VT/profile:3704.yml```

---
### Submit

Upload the following on Canvas:
- [ ] A screenshot of a successful configuration check

Other grading checks:
- [ ] You are expected to complete the syllabus survey, which will be graded from the form responses.
- [ ] Your introduction will be checked on Mattermost.

**Due:** Friday (9/4) at 11:59pm
