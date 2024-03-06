## GitHub-Jira Integration For Automation of Jira-Tickets

The **GitHub to Jira Ticket Automation** project streamlines the process of managing software development tasks by automating the creation of Jira tickets in response to comments on GitHub issues. With this integration, developers can seamlessly transition discussions and tasks between GitHub and Jira without manual intervention.

### Project Overview

The project consists of a Python function hosted on a Flask server, deployed on an AWS EC2 instance. A GitHub webhook is configured to trigger the Python function whenever a comment is made on any issue within a GitHub repository. The Python function processes the webhook payload, extracting relevant information such as issue title, body, and commenter's details. It then utilizes the Jira API to create a corresponding ticket in a specified Jira project, populating it with the extracted information.
