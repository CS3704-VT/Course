# CS3704 CI/CD Activity (11/3)

In modern fast-paced software development, automation plays a crucial role in enhancing team collaboration and efficiency. Development bots, particularly those integrated within communication platforms like Slack and Mattermost, facilitate real-time updates, notifications, and interactions that streamline workflows. For instance, prior work shows the primary reason developers use Slack is for development and deployment support.[^1] By automating routine tasks and sharing critical information seamlessly, these bots enable teams to focus on higher priority tasks and reduce manual efforts. For this assignment, you will create your own Mattermost bot that integrates with your Project 2 Continuous Integration/Continuous Deployment (CI/CD) pipeline.

## Initial Activity

_Reflection:_ To kick off this workshop, write a brief reflection on your experiences with CI/CD and development bots. Discuss with your group which CI/CD platforms, bots, and development tools you have experience with, and how bots in general might improve (or worsen) development practices.

## CI/CD 

_GitHub Actions:_ Complete the [Quickstart Guide for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) to learn how to create an initial CI/CD pipeline for a GitHub repository.


## Mattermost Bot

First, follow the steps to create an **[Incoming Web Hook](https://developers.mattermost.com/integrate/webhooks/incoming/)** for Mattermost. Incoming webhooks post messages to Mattermost based on an external trigger, while _outgoing webhooks_ use Mattermost content to trigger external applications. You should have access in the class Mattermost instance to create a webhook for the Town Square channel. You may customize the message if desired.

After you follow the initial instructions, modify the initial template text to include your response to the discussion question above. Then run the generated `curl` command to post a message in our Mattermost channel. **Each student must post a message answering the overview question in the Town Square channel from your profile as a `BOT` account to receive full credit!**

## Reflection

_Reflection:_ After completing the Mattermost Bot, as a group discuss the advantages and disadvantages of this type of bot and whether or not it would benefit your development workflow. Also discuss what other checks you want included in your CI/CD pipline (required for PM2.3). Based on your group discussion, you can decide whether to keep the Mattermost bot or not after this assignment is submitted (see below).

_Project 2 Integration (optional):_ Using what you learned from the initial incoming webhook creation, create a Mattermost Bot that reports project build results every time the CI/CD pipeline is run for your project. If you haven't already, you will first need to create a separate Mattermost channel for your Project 2 team (or can create a new web hook for whatever communication platform your team uses). Then, add an incoming webhook into your GitHub Actions workflow. Potential information your bot could report includes testing outcomes, commit messages and details, build status, static analysis tool results, etc. You can also feel free to enhance your bot or add other features and ideas. For extra credit (PM2.3), submit screenshots of the required CI/CD pipeline output in your team channel, along with reflections from each team member on whether or not this bot was useful and would be worth keeping for the remainder of the project.

**Submission**: Your submission should include: (1) an individual reflection as a Mattermost bot message from each student (this will be checked in Mattermost); (2) a summary of your pre and post reflection discussions with _insights from each team member in class_ (upload on Canvas).

**Due:** Tuesday, November 3 at 11:59pm

[^1]: Bin Lin, Alexey Zagalsky, Margaret-Anne Storey, and Alexander Serebrenik. 2016. Why Developers Are Slacking Off: Understanding How Software Teams Use Slack. In Proceedings of the 19th ACM Conference on Computer Supported Cooperative Work and Social Computing Companion (CSCW '16 Companion). Association for Computing Machinery, New York, NY, USA, 333–336. https://doi.org/10.1145/2818052.2869117