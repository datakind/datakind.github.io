---
layout: default
title: Evaluating Bias
date: 02/29/2024
author: Benjamin Kinsella, William Ratcliff, Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: execute
---

In the Design Stage the team considered [project risks](/project-stages/design/project_risk_and_ethical_assessment), [data inclusion](/project-stages/design/evaluating_data_inclusion), and [community accountability](/project-stages/design/consulting_additional_key_stakeholders). Having thought carefully about potential risks and outlined mitigation strategies, you’re now at the Execute Stage and must continuously revisit and evaluate bias in your proposed technical solution. There are not only risks associated with data inclusion and model trustworthiness, but also biases to be considered during general project management and execution. 


There are an abundance of guides and best practices on machine learning ethics and bias. Since the landscape is constantly changing, we are not going to offer a comprehensive resource list or a one\-size\-fits\-all guide, but feel free to refer to [this toolkit created by DataKind UK](https://datakind-ai-ethics.netlify.app/#/) that summarizes the advantages and disadvantages of a few popular responsible data tools. As a DataKind volunteer, use your expertise, do your own research, and find the best resources or tools for your specific project. Regardless of the tool that you may choose to use, here are some questions and considerations as you move forward in executing your project. 


##### Bias and General Project Execution Principles


Bias doesn’t just arise from technical solutions and machine learning models, but also from project processes, human context, and more. While this list is not exhaustive, consider the following questions throughout the project's execution:


* What cognitive biases are likely to emerge given team dynamics and scope of project? For example:
+ Survivorship bias: Is there a tendency to overlook some variables because of their lack of visibility? In what ways could the team concentrate on features (e.g., people, processes, etc.) that make it past some selection process and overlook those that did not?
+ Availability bias: Is there a tendency to consider certain features or processes as more representative than they actually are? Have you worked with the Project Champion and/or other subject matter expert to consider additional information, ideas, and feedback during the Execute Stage?
+ Confirmation bias: Have you considered ways in which project findings are interpreted as confirmation of beliefs? Have you sought after disconcerting evidence or additional perspectives to improve your solution?

* Are team members appropriately assigned tasks based on their skill sets and backgrounds? Do tasks fit within the scope of volunteer requirements?


##### Bias and Machine Learning Outputs


Some of the most common data science projects you’ll encounter at DataKind involve some use of machine learning or statistical modeling (e.g., regression modeling, decision tree learning, random forest, etc.). Since these algorithms are generally used to predict, estimate, or classify target variables, they present several potential sources of bias. There are several common approaches to assess models and their potential biases. Regardless of what tool or model you use for bias evaluation, here are some questions that need to be asked for every DataKind project:


* Have you questioned the interpretation of your model’s results? How can you numerically define bias within your model?
* What power dynamics are relevant within your project? How might they be characterized in the data?
* Is the data about a group, which was collected by “outsiders” (i.e., non\-community members) to make certain behavioral changes?
* Have you thought about how intersectionality might impact the data and model output? Consider evaluating for [differential fairness](http://jfoulds.informationsystems.umbc.edu/papers/2019/Foulds%20(2019)%20-%20DifferentialFairness_NeurIPS_MLWG.pdf).
* How well does the training data match to the test data?
* Is there under or over performance? Is a model overfit or underfit? Have you looked at the bias variance trade\-off and carefully decided on where to fall on the spectrum?
* Have you considered the construct validity of your model? That is, does your outcome of interest pertain to a theoretical construct, such as well\-being, trust or happiness? How is this outcome being measured (e.g., self\-reported, inferred from observation, etc.)?
* Have you considered the historical context of your project and its data? Is there a reason to believe that a certain group of people are underrepresented or systematically excluded in the data? What types of harms should you anticipate? For example: Are you working in digital or financial inclusion? How might financial records construct measurements of credit worthiness? What risks could emerge from a biased model (e.g., redlining individuals, creating tools that could be used for predatory loans, etc.)?
* Have you considered different types of harms that could come from your model’s output? For example: How might your model cause harm in a user’s quality of service \- that is, when a group of people gets a lower quality service, product, or information? How might your model cause allocation harm \- that is, the potential for a solution to deny access to products, services, or information for groups of people? Could the model propagate harmful stereotypes or beliefs? If the model is discovered to cause harm to a group of people, is there a mechanism to take the model offline and provide recourse to those affected?


##### Bias and Other Data Considerations


While machine learning methods are common in many DataKind projects, you will naturally encounter a range of different analytical approaches and methodologies. Regardless of the method chosen, the ways in which you present your initial analyses to your teammates and the partner organization may lead to biased decision making. While this list is not exhaustive, here are some topics to consider as you prepare your analyses and share them with the team:


* Are your analyses comprehensive of trends across certain populations (e.g., missing data due to patient attrition, etc.)?
* Can you ensure that your data accurately represents those you are serving and is not missing any people, variables, communities, or indicators? Are there sufficient examples to mitigate risk of misrepresentation in data? Could aggregate data cause certain individuals to be excluded from the data? (See [Data Inclusion](/project-stages/design/evaluating_data_inclusion) article for further discussion.)
* Have you considered the impact of non\-response bias and voluntary response bias in your data collection, particularly in survey or feedback form\-based projects? Non\-response bias arises when individuals choose not to participate or drop out of the study, potentially skewing results. Similarly, voluntary response bias occurs when respondents must opt in, which may not accurately reflect the wider population. How might these biases affect the representation and validity of your findings, and what measures have you taken to address or mitigate their impact?
* Are you clear about sampling errors and variation in your data set? Have you reported and communicated summary statistics, including the data’s variance, confidence intervals, margins of error, etc.?
* Have you considered ways in which your visualizations and data analyses might be misinterpreted? For example: Are there any design choices in your visualizations that could lead to incorrect conclusions? Are there mismatches between perceived color differences and actual data differences? Are the axes truncated? Did you perform any transformations on your data that could distort interpretations?
* For geospatial projects, have you evaluated ways in which your maps may lead to false conclusions or bias? For example, does projection bias \- the tendency to mis\-portray the actual size of locations \- diminish relative size and importance of a country? Does your map fail to represent people or land that has been implicitly or explicitly excluded (e.g., misrepresenting population level characteristics through aggregation, etc.)?