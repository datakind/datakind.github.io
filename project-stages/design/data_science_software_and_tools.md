---
layout: default
title: Data Science Software and Tools
date: 02/29/2024
author: Neal Fultz, Arina Igumenshcheva, Nathan Banion, Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: design
---

As you design your project, you’ll reach a point where you’ll need to decide what data science tools to use. As you assess whether a tool is a good fit for this project, consider:


* Is the tool standard in data science?
* How much money does the tool cost?
* Is the tool associated with any restrictive licensing terms?


##### Selecting a Programming Language


There are a lot of tools that industry professionals recommend data scientists use (and the list grows every day!), but let’s focus on the foundational tool that you need team and partner organization buy\-in for: the programming language.


Typically, data scientists conduct their modeling and analysis by coding in programming languages rather than via a graphical user interface (GUI), because:


* It’s easier to perform complex data manipulations using a language rather than through a point\-and\-click interface.
* Having your analysis in the form of code makes it easier to reproduce and share with collaborators.


(RStudio’s Hadley Wickham has an [interesting talk about this](http://youtube.com/watch?v=cpbtcsGE0OA&t=2694s).)


The most popular languages for data science are currently [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and [R](https://en.wikipedia.org/wiki/R_(programming_language)) due to the fact that:


* **They support a large ecosystem of statistical and numerical computing software.** The more tools that the language supports (e.g. deep learning libraries such as [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow), the more statistical methods and technologies you’ll have at your disposal during project execution.
* **There are a lot of professionals who know these languages.** This makes it easier to find qualified volunteers for your project.
* **They’re free!** That's right \- the right to use them costs $0\.
* They support maintainable package development, with good tools for unit testing, dependency management, and high quality documentation.


You can choose to use either, but we recommend that you stay consistent within each project team so that your volunteers can collaborate efficiently. Choose what works best for your partner organization, in order to enable them to sustain the results.


##### Cost of the Tool


There are a couple of ways that cost can be raised as an issue as you design your project. The first scenario is when your partner organization uses software that requires some sort of paid license. Common examples include:


* **Proprietary Languages or Computing Environments** \- Staff in the partner organization may be familiar with writing code \-\- but only in a proprietary language such as [Stata](https://en.wikipedia.org/wiki/Stata) or [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
* **Business Intelligence (BI) Tools for Enterprise** \- Staff in the partner organization may analyze their data in a proprietary point\-and\-click tool such as [Tableau](https://en.wikipedia.org/wiki/Tableau_Software).


It’s likely financially infeasible to provide volunteers with paid licenses, but check with your Chapter Leader or DataKind staff support if it would be hugely helpful for a project. Luckily, with skilled volunteers and good project management, the volunteer team can avoid having to use these paid tools in most cases. For example, even if a Stata or MATLAB\-user from the partner organization wants to understand project code, the code could still be written in R or Python. A skilled volunteer who’s good at explaining technical concepts and possesses good coding hygiene can be paired with the MATLAB user, gradually increasing the MATLAB user’s comfort level with R or Python. **When deciding on tooling, it is important to clarify with the organization if they want to be able to reproduce the analysis or if they just want the insight itself** or language\-neutral versions of the data (e.g., csv) and analysis steps (documentation). 


The second scenario involves the need for [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) (computation using servers in remote data centers). Popular cloud computing platforms include [Amazon Web Services](https://en.wikipedia.org/wiki/Amazon_Web_Services), [Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure), and [Google Cloud Platform](https://en.wikipedia.org/wiki/Google_Cloud_Platform). These all require money, and the cost may be nontrivial. Situations when cloud computing may be necessary include:


* **Big Data** \- There’s too much project data to process on a personal computer. Dedicated computational resources are required.
* **App Hosting** \- The output of the project is a software application that needs to be hosted on a server somewhere.


Discussions around cloud services can get tricky because how important they are varies on a project\-by\-project basis, and consensus needs to be reached in terms of who pays for it. An important tip is to be cognizant of what cloud services constitute a one\-time cost, and what services constitute a recurring cost. If the cost is recurring, the partner organization will need to possess financial means to support the tool’s upkeep beyond the duration of the project. Make sure the potential cost is understood and agreed upon upfront, so that the DataKind team does not build a product that is not financially sustainable for a partner organization. If this will be a one\-time cost and the partner organization is unable to pay for it, talk to your Chapter Leader or DataKind staff support to determine if DataKind would be able to pay for it, which we may be able to in rare cases. 


##### Licensing


If you decide not to use an open source tool, remember to ask the partner organization whether they have concerns about licensing restrictions. This is because output produced by a tool with a certain license may be bound by certain ownership and sharing restrictions.


When in doubt, consider either consulting legal personnel or defaulting to a tool that uses a permissive open source license. If you consider the latter route, check out this page by the [Open Source Initiative](https://opensource.org/licenses) for more details. This is also a great topic to discuss with your DataKind staff support person.