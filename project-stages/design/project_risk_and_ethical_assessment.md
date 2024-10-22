---
layout: default
title: Project Risk and Ethical Assessment
date: 02/29/2024
author: Benjamin Kinsella, Manojit Nandi, Daniel Nissani, Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: design
---

Assessing and mitigating risks is imperative in any data science project. In addition to the strategies outlined in the [evaluating data inclusion article](evaluating_data_inclusion), use the following tips and considerations as you assess the ethics and risks of your potential project. Keep in mind that this guide is not meant to be comprehensive. Let the examples and suggestions below inspire you to think carefully about risks and determine your own evaluation approach that will ensure you are prepared to produce products that will be used for good.


##### Ethical Technology Implementation


Think carefully before proposing any technical solution. For example, we typically do not build tools that automate any decision making, but instead choose to build a recommendation system that allows the decision to still be made by a human. 


##### Balancing Technical Trade\-offs


There are also several technical considerations that the volunteer team must take into account. Identify the appropriate tradeoffs with software decisions. For example, think carefully about the trade\-offs between using open source versus proprietary tools to build your solution. Additionally, when deciding about tools, ask questions about accessibility: Can the solution work in a resource\-constrained environment? Can it be equitably accessed? 


##### Assessing Financial Implications


There are also potential financial costs associated with computational and project resources for many DataKind projects. Make sure these costs are evaluated and their trade\-offs have been acknowledged. Many of the inputs for your data science solutions are expensive, so you will need to assess these costs of your project and determine which trade offs are necessary when designing your project. For example, think about the cost of computational resources (cloud computing is expensive) and time spent on a project for staff. Understand the time commitments and trade\-offs that you will face when working with your Project Champions. 


##### Evaluating Model Fairness


Make a plan to check the model robustness per demographic group. Does slightly changing the input features change the end outcome more often for one demographic group compared to another? For machine learning models, plan to calculate global error metrics (e.g., RMSE, AUC, precision, recall) as crosstabs of specific demographics. For example, the model has an RMSE of 1\.9 globally, but an RMSE of 5 for low income observations. Understand why and how the model can be gamed or used.


##### Consider Employing third party tools for Model Fairness


Following the evaluation of model fairness, leveraging tools like [Google's AI Fairness Indicator](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_Example_Colab) and [IBM's AI Fairness 360 (AIF360\)](https://aif360.res.ibm.com/) can significantly aid in identifying and mitigating bias. These free tools offer a variety of metrics and methods to ensure equitable outcomes across different demographic groups. Specifically, in projects aimed at social impact in humanitarian spaces, they help highlight discrepancies in model performance and guide necessary adjustments to foster inclusivity and fairness. 


##### Communicating for Accuracy


Create and commit to a clear communication plan to ensure that output of a project will always be interpreted correctly with the missing data noted upfront in any reports, visualization, or decision making based on the data. Document and caveat any assumptions made and what that implies for outputs.


##### Design for Sustainability


One often overlooked risk is that the project won’t be sustainable within the partner organization, so taking time to proactively mitigate that risk during the design stage is essential. Questions to consider when thinking about sustainable design include:


* Does the organization have a history of data driven decisions?
* What are the environmental conditions of the final solution? (e.g. is this on a mobile phone in a place with no electricity?)
* How fast will the solution be outdated?
* Who will own the product after the project is complete?
* What will it take to sustain the product, and is there a plan in place to make sure that happens?
* Is the organization prepared to support the product after the project is complete?
* Is the organization ready to accept and integrate the results even if they reflect potentially uncomfortable deficiencies or changes in how they operate?
* Have you and the Project Champion together reviewed the project risks outlined in this article?


Whether the answers to these questions are deal breakers on conducting the project varies depending on context. Still, no DataKind project starts without ensuring there is a plan in place for the organization to sustain and use the project after DataKind leaves! 