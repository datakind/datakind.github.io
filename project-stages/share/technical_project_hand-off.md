---
layout: default
title: Technical Project Hand-off, Systems Integration, and Supporting Initial Implementation
date: 02/29/2024
author: Benjamin Kinsella, Emily Yelverton, Kelson Shilling\-Scrivo
audience: DataKind Volunteers
category: project-stages
subcategory: share
---

​​Since you aren’t the one who will be using the product you built, one of the most important things you will do is hand off your project’s deliverables and documentation to the partner organization. Doing this process well is critical for the project’s long\-term sustainability, so take time to organize your code, write up any findings, and create as standalone of a package as you can. 


The Project Manager should own this process and make sure the team follows the best practices outlined below. Handoff is when the technical component of the project is “completed,” but that doesn’t mean you are done with the engagement and the full cycle of the project! The rest of the Share and Evaluate stages are extremely important, so it’s essential to take time during the handoff and systems integration process to clarify that your engagement with the partner organization is not actually done yet.


##### Preparing code and documentation for handoff


Handing\-off code and technical files should be completed in the format requested by the technical project owner or the data specialist at the partner organization. Make sure the documentation is usable to whoever at the partner organization will be taking the project forward. Preparing for hand\-off is a great time to check in on implementation of GitHub wrap\-up best practices, code cleaning, and clarity of all documentation. These steps include:


* Make sure the ReadMe is written and sufficiently detailed such that someone can come in cold, clone the repo, and run the code.
* Close any open issues or pull requests, merge any branches or note why they are kept un\-merged (e.g. not needed or still in development).
* Attempt a fresh installation of code, note any errors, and add their potential solutions to the documentation.
* Make sure the code can run in the target environment!
* Review the article on [instructional materials](/project-stages/execute/documentation_and_instructional_materials) to ensure you have done everything needed to enable the Project Champion to sign off on the received deliverables.


Remember, the goal is to test any outputs from the partner organization perspective prior to final hand\-off. Partner organizations may have limited technical expertise or domain understanding to troubleshoot after the solution handoff. Therefore, make sure to review the deliverables from the point of view of someone with minimal background on the project and technical expertise. As a final check before hand\-off, have the technical project owner test\-run your code. This will uncover any steps in the workflow that are confusing to the end\-user and may uncover some technical “holes” that need to be plugged. 


##### Discuss the code lifecycle


No code withstands first contact with production (at least not indefinitely). Now is a good time to discuss with the project owner the following questions:


* Are there inputs that are likely going to change? Is the code easy to modify to account for that?
* How long will this code be needed to work for? Was this project a one\-off consulting output or will the product be used in the long\-term? If long\-term, is there a model and/or code maintenance strategy?
* Revisit your definition of “done” and definition of “success”: Is code complete enough to be successful? Will the code last long enough to be successful?
* If this project is successful, are there opportunities for future collaboration? Discuss ideas to extend code for more use cases, or tackle a related problem.


**Handing over the technical materials**


1. In a final presentation to the Project Champion and a technical member of the partner organization:
	* Explain what your team did and why the solution matters for the organization (e.g. did your solution increase the organization's capacity to serve more individuals, or allow them to make better decisions?)
	* Clearly outline your team’s deliverables, process, key findings, and recommendations
	* Explain what their next steps are, and who is responsible for the next steps, to ensure the project provides its full value
2. Give the Project Champion plenty of time to review the project documentation and ask questions
3. Set up time for all stakeholders at the organization to meet with the Data Ambassador, Project Champion, and potentially other team members as well for training and to get their questions answered.
4. Agree on next steps and plans for the Share and Evaluate Stages. You may consider leaving a Slack channel open so the Project Champion can reach volunteers to ask questions.


##### Supporting Initial Implementation


While the specifics will vary based on project needs, here are a few ways that Data Ambassadors have ensured their partner is set up for adoption and sustainability:


* Assist with the set up and integration of the model within the partner organization's existing data management systems, so that it can be used automatically
* Share your email address with the data specialist and encourage them to reach out if they have any follow\-up questions
* Provide maintenance and troubleshooting for a tool for a few months after project completion, and explain to the data specialist what you did every time you fixed an issue that came up


To conclude, part of the scoping process is making sure that the project will be sustainable, and the project deliverables were carefully designed to ensure that specific teams and individuals at the partner organization would be able to manage them. You shouldn’t be teaching someone python or to use AWS at this stage. If you feel that there has been a mismatch of the deliverables and that the partner organization will not be able to sustain the project without extremely substantial support, talk to your DataKind staff support to troubleshoot and plan how to move forward. Read more about sustainability planning in this Playbook article on [instructional materials](/project-stages/execute/documentation_and_instructional_materials).