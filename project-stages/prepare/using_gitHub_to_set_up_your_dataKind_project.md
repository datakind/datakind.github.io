---
layout: default
title: design
date: 02/29/2024
author: Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: prepare
---




**Intended audience:**
DataKind Volunteers






#### Using GitHub to Set Up Your DataKind Project


This article documents GitHub’s Actions template, developed for DataKind to assist your project work. It includes a summary of how to use GitHub’s action templates and how to contribute for future improvements of the project. 


##### What are GitHub Actions?


GitHub Actions help you automate tasks within your software development life cycle. GitHub Actions are event\-driven, meaning that you can run a series of commands after a specified event has occurred. For example, every time someone creates a pull request for a repository, you can automatically run a command that executes a software testing script. See this [summary of Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) to learn more.


##### The Actions Template


We created an [Actions template](https://github.com/migarjo-enterprise-org/initial-actions-template/blob/main/README.md) and [forked it onto to DataKind’s GitHub repository](https://github.com/datakind/initial-actions-template-DataKind) (see Figure below). 


![Template view on DataKind GitHub workspace](assets/img/action_template.png)
This demo repository to create Actions would run on a newly\-created repository. It contains the following two actions:


* Create first issue: This runs after the first commit on a newly\-created repository based on this template. It creates an issue instructing users to perform some first steps
* Customize repo: This is a manually\-initiated Action that will clone a repository based on selected inputs, and copy its contents into this repo.


Note: Since the "Customize repo" action clones another repository other than this one, it requires an additional Personal Access Token that has access to any repos that need to be cloned. To enable this, create an Actions Secret at the organization level with a PAT scoped to "repo". The key for this token should be GH\_ORG\_TOKEN.


##### Want to contribute?


As we begin to use Actions within GitHub at DataKind, there are improvements to the template that we are hoping to make. Are you testing and validating the template with your DataKind project? Let us know what you learned and how it can be improved by commenting on this article below! We have a few ideas for how volunteers can contribute to improve the way we use GitHub Actions. This section of this Playbook article outlines those ideas for improvement, so that (if you want to extend your volunteering to help others at DataKind), you can make the changes and enable other DataKinds to work even better. 


First, the yaml file creating the repository should be updated to ensure the template produces the most convenient and usable GitHub repo. 


![Template view on DataKind GitHub workspace](assets/img/yaml_file_1.png)
Additionally, part of the template allows for the selection of either Python or R as the default programming language. There is an option to select a specific project category (Project A, B, C, etc.), such as a predictive model, software/product design, etc. We are working on refining and defining these categories to those that will be most usable across all DataKind projects. Share your ideas in the comments below!


![Template view on DataKind GitHub workspace](assets/img/yaml_file_2.png)
If you would like to volunteer to build out the next steps of this project, feel free to join us on GitHub! Reach out to us by pushing the “Provide Feedback, Ask Questions!" button to the left with any questions you have.


##### Relevant links:


* [How to use GitHub accessibility settings](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/managing-accessibility-settings) (tailor to your vision, hearing, motor, cognitive, or learning needs)
* [Template on DataKind’s GitHub](https://github.com/datakind/initial-actions-template-DataKind)
* [Demo video](https://drive.google.com/file/d/18a0KrAbRBzQyt6phHadjRqXPuPRk-q43/view?pli=1) of how the DataKind GitHub Actions would work
* [Learn GitHub Actions Tutorials](https://docs.github.com/en/actions/learn-github-actions)
* [Introduction to GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
* [Essential Features of GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions)
* [Sharing secrets with an organization](https://docs.github.com/en/actions/using-workflows/sharing-workflows-secrets-and-runners-with-your-organization#sharing-secrets-within-an-organization)
* [Actions reference material](https://docs.github.com/en/actions)
* [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
* [Context and Expression Syntax](https://docs.github.com/en/actions/learn-github-actions/contexts) (This covers the metadata provided to the Actions environment for use in your automation, as well as syntax for how to use them.)
* [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)



 **Contributer(s):** Caroline Charrow, Rachel Wells







##### Contact us


If you would like to learn more about us, partner with us, or get in touch, email us at community@datakind.org



 
**Subscribe to our newsletter**
  

[Subscribe](https://www.datakind.org/subscribe/)



