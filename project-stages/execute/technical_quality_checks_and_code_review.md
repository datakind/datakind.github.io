---
layout: default
title: Technical Quality Checks and Code Review
date: 02/29/2024
author: Benjamin Kinsella, Matthew Harris, Srivalya Elluru, Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: execute
---

While you are building your minimum viable product and final solution, take care to ensure your solution is technically correct as you go. What this means will vary based on the project, but all projects should include:

* **Intuition checks:** Step back and think about the data and results you are getting. Does the data look right? Does it follow what we’ve heard for our projects? Does anything not add up?
* **Reality checks:** You have already asked the question, “does the proposed solution make sense?”. Now we need to ask, “do the drafted outputs make sense?” as we build. Continuously check\-in and reflect on if the output makes sense for the partner. This includes constantly asking yourself “is this a solution the partner organization will be able to implement?”
* **Documentation checks:** You already know you need to keep your project documentation up to date, but this check is about technical documentation. This includes:
+ Check the operation system specs, such as important prerequisite software installation commands, a requirements.txt or .json file listing all the dependencies with versions, and a log.
+ Check the README for essential information, such as a directory structure description, what each file is responsible for, steps on how to run the code, and where the logs get printed.
+ Check the code for all the quality elements outlined in [Coding and Working with Data at DataKind](/project-stages/execute/coding_and_working_with_data_at_dataKind).


For predictive projects, we should consider a few more essential items: 


* **Methodology checks:** These are essential to make sure the basics of what you are doing is the right choice. Double check all your model’s assumptions. Think carefully about the model’s propensity for overfitting or underfitting. Consider the bias\-variance tradeoff, and make sure you made the right decision in your model selection. Run the methodology by another statistician that you trust.\* When one of your checks results in something that doesn’t make sense, discuss the challenge with your team and together brainstorm a solution to verify.
* **Performance metrics:** Identify and produce standard performance metrics for your project's output, such as accuracy, running time, and resource consumption. For example, for predictive models, you want to ensure that the probabilities and confidence score estimates produced by various algorithms are good in order for the particular to reliably deploy interventions.
* **Reproducibility checks:** Make sure that the results produced are fully reproducible. This is particularly important if the project is producing assets which might be used in further projects. Try using these assets on a different machine. At a minimum, ensure data requirements for reproducing the results are clearly documented. This is a good solution for cases where reproducing the results requires access to secured data.


 Don’t be afraid to raise a hand and point out the issue you found or the question you have. 


##### Final Technical Checks


Lastly, in addition to the above technical reviews, make sure you carefully review project deliverables and documentation as you prepare to hand your deliverables over to the partner organization. This is one of the last chances to review your final deliverable to make sure there are no errors or bugs! There are three components of the technical project review before sharing the deliverables with the project partner:


1. **Basic code quality and cleanliness review:** Check for small errors, typos, and overall clarity of comments and structure. For projects that include volunteers with a variety of skill levels, code review is a great task for volunteers with coding skills who might not have extensive methodology knowledge. For small DataCorps teams, pairing up teammates with matching skills and having them review each other’s work tends to be effective.
2. **Reproducibility review:** Check that the analysis and deliverables can be reproduced easily. Avoid “well, it worked on my machine!” by testing to make sure it also runs on someone else’s machine. For example, a package installation or setting the seed can be easily forgotten in the setup code. Running the code on a different machine is a quick check that can prevent a lot of headaches with the partner organization.
3. **Technical documentation review:** This step is best done by having additional reviews conducted, preferably by someone not involved in the project\*. Reach out to the DataKind volunteer community on slack to see if anyone might be willing to do a review for you! By looking at the documentation with fresh eyes, the reviewer wants to ensure that everything (e.g., code, instructions, etc.) is clear and understandable. This review simply involves reading the technical documentation, asking whatever open questions or clarifications it leads to for understanding, and then the project team updating the documentation based on the questions asked. The goal of the technical documentation review is to ensure that someone could onboard to the project results without being involved in the project at all.


\*When running the methodology or documentation by someone outside the team, we first advise using someone inside the DataKind network who already has a signed NDA on file with us. We have tons of brilliant volunteers eager to contribute to projects as advisors and provide one\-off support in this way. Post on the slack \#help\-wanted channel the type of challenge you are addressing, and you’ll likely be able to find a great expert to conduct a methodology check for you! If you want to talk with someone outside of DataKind, talk to your DataKind staff support in advance, to make sure you are complying with our partner agreements. Make sure to speak in extremely general terms about the project constraints and requirements that were used in model selection. Stick to information in the agreed upon public language section of the Project Brief. If there is any risk that you might operate against the NDA in conducting a methodology check with a statistician you trust, talk with your Chapter Leader or DataKind staff support, and the team can get your advisor an NDA to sign.