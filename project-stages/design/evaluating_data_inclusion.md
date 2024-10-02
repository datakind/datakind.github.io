---
layout: default
title: design
date: 02/29/2024
author: Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: design
---




**Intended audience:**
DataKind Volunteers






#### Evaluating Data Inclusion


Data inclusion ensures the data are representative and are not missing any people, variables, communities, or indicators. Evaluating possible data inclusion risks means understanding the assumptions that are made when collecting, curating, or tagging data by evaluating the abstract notions of data, what’s included, and decisions that were made in collection. 


At DataKind, we never build algorithms where the user provides an input and receives an output, but without being able to see or otherwise understand the inner workings of the algorithm that produced the output. We avoid situations where variables like race, gender, ability, sexual orientation, among others \- including their proxies \- cannot be tested in a transparent way. Instead, we opt for interpretable algorithms when it comes to people. Proxies can be identified if domain experts can “guess” at protected characteristics or PII from the information. If this data is missing from your dataset, it might make it difficult to evaluate your model for underlying and unintended bias. How will you know you have an algorithm that excludes women, if you don’t test your model for gender inclusivity? Make sure you have the variables you need in your data set to test for inclusivity, but ensure that your plan does not include using these variables in a model that cannot be interpreted. 


An example of data exclusion is health outcomes data in [DHIS2](https://dhis2.org/), a health software used for data tracking. Consider an instance in which only data from health facilities in Kenya were reported. These data may represent certain groups within the Kenyan population, but only for those who have access to healthcare. That is, these data only include formal healthcare transactions and not from informal cases in rural populations. Another example is that data collected by randomly selecting household addresses or aggregated at the zip code level, which is meant to be representative of the whole population, often excludes the homeless. Any data collected digitally could exclude those who are not engaged on these platforms.


Below are some common questions to consider when approaching data inclusion efforts with your project. 


##### Data Provenance


Understand and interrogate how dataset was created or composed 


* For what purpose was the dataset created? Was it for a specific task or initiative?
* Who collected the data (e.g., a specific team or research group, field workers, etc.)?
* How were the data collected? Were data acquired automatically, such as through web scraping, character recognition, behavioral data, etc.?
* What incentives do the data collection agents have in reporting? Might somebody (consciously or subconsciously) be manipulating data to meet objectives?
* If using pre\-trained data from outside the partner organization, where do the data come from? What assumptions are made when using pre\-trained data to answer project\-specific questions? What potential biases may arise from using pre\-trained data?


##### Data Inclusion and Disparities


Identify and evaluate who is missing from the data 


* Is there anything about the dataset and the way the data were collected, preprocessed, cleaned, and labeled that might impact the dataset’s future uses? How might these composition mechanisms negatively impact the way you intend to use data?
* What variables are missing that might help you identify who is missing from your data set and check if it is truly representative and inclusive (e.g., race, gender, sexual orientation, etc.)? If possible, compare aggregated population statistics to the sample data in order to understand skews across demographics. Do you notice any differences? (e.g., population is 50% female, but data is 75% male) Note the global nature of DataKind projects, such that many protected categories like race differ by country.
* What variables may be problematic to include in a model (e.g. race, gender, etc.)?
* Did you detect anomalies during the Data Audit that may inform your execution plan?
* Are there biases in the sample selection or variables made available? Interrogate available data and search for potential biases and limited representativeness of the problem. Keep [differential fairness](http://jfoulds.informationsystems.umbc.edu/papers/2019/Foulds%20(2019)%20-%20DifferentialFairness_NeurIPS_MLWG.pdf) and intersectionality in mind as you evaluate the data.
* Consider additional technical approaches to mitigate challenges with missing data (e.g., resampling). What approaches can you take to mitigate or estimate missing data? For example:
+ Estimate the missing data using techniques, like interpolation (only use this option if you can do so with strong accuracy!)
+ Sample down to create a balanced class dataset that is equal to the population served
+ Create augmented data that adds in those excluded observations (carefully, with subject matter expert support)
+ Missing Data (Nulls): impute mean, regress a value (if correlated with other values, leave null if informational, or throw out if missing at random)


##### Subject Matter Expertise and Project Specific Issues


Incorporate domain expertise and previous research to ensure data representativeness and inclusivity.


* What domain expertise does the partner organization have to ensure data representativeness and inclusivity? What historical context can the partner organization and other domain experts provide to ensure that no group is underrepresented or systematically excluded in the data?
* What types of harms can be anticipated from using your methodology, including previous research done in similar contexts? For example:
+ Does the model provide allocation of a particular resource?
+ Could the model propagate harmful stereotypes or beliefs?

* Does your outcome of interest pertain to a theoretical construct (e.g. well\-being, trust, happiness) that requires subject matter expertise to assess or interpret?
* How is the outcome of interest being measured (e.g., self\-reported, inferred from observation)? Ensure construct validity by working with your partner organization and other domain experts to question model assumptions.
* Is there anything that the partner organization might need to know to avoid, which could result in unfair treatment of individuals or groups?
* Could the model have unintended consequences for certain groups?
* If the model is discovered to cause harm to a group of people, is there a mechanism to take the model offline and provide recourse to those affected?
* Could the model be used for nefarious purposes? For example, could a tool made to predict student dropout rates be used to exclude \- not support particular at\-risk students?
* Would it be possible to misinterpret the data and results?
* Would the end users be able to understand the proposed output?


##### Additional resources:


* Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J., Wallach, H., Daumé III, H., and Crawford, K. (2018\).  [Datasheets for datasets](https://arxiv.org/pdf/1803.09010.pdf). arXiv preprint arXiv:1803\.09010\.
* Suresh, H., and Guttag, J. (2019\). [A framework for understanding unintended consequences of machine learning](https://arxiv.org/pdf/1901.10002.pdf). arXiv preprint arXiv:1901\.10002\.
* Jacobs, A. (2021\). [Measurement and fairness](https://arxiv.org/pdf/1912.05511.pdf). In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (pp. 375\-385\).


 **Contributer(s):** Caitlin Augustin, Benjamin Kinsella, Emily Yelverton, Jeremy Osborn, Manojit Nandi, Daniel Nissani, Phil Azar, William Ratcliff, Mallory Sheff







##### Contact us


If you would like to learn more about us, partner with us, or get in touch, email us at community@datakind.org



 
**Subscribe to our newsletter**
  

[Subscribe](https://www.datakind.org/subscribe/)



