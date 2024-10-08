---
layout: default
title: GenAI Use Case Selection and Risk Assessment
subtitle:
date: 02/29/2024
author: John Harnisher, Matt Harris, Lindsey Washburn, Kathleen Yaworsky
audience: Social Impact Professionals
category: social-impact
subcategory: genai
---

Once you’ve made your way through steps one through four in the Playbook article “Getting Started with GenAI,” you might be ready to evaluate and select your first GenAI use case. This article is intended for anyone at social impact organizations engaging in the strategic design and decision making around GenAI use cases and risk mitigation, accessible and useful to both technical and nontechnical audiences.


To get started on brainstorming, a few use cases that are generating the most enthusiasm across the social sector include:


* **Personalized service delivery**: A particularly common use case for educational/training content is identifying the right modules or material to provide to the end user next based on their experience. But this also applies to many different types of social impact organizations, including for tasks like supporting local campaigners with localized information from data analysis, job matching, and interview prep. Although most exciting, this use case is also the most risky. Often, when social impact organizations evaluate using GenAI for this, they end up deciding that the needed guardrails and risks outweigh the benefits for now.
* **Data science**: Using GenAI can supplement and speed up technical work, although data and coding skills are still required by the end user for fact checking and code reviews. With that in mind, GenAI can provide assistance with:
	+ Data cleaning, database wrangling, quality checks, etc.
	+ Data analysis, qualitative text analysis, summarizing research, etc.
	+ Metadata prediction, labeling data, codebook creation, etc.
* **Knowledge management**: GenAI is fantastic at navigating many resources to find and/or summarize the most relevant information. There’s a common challenge of it being overwhelming for staff or users to find the resources they need, and GenAI can speed up the process.
* **Content creation**: GenAI can be used to create curriculum, images, communication materials, presentations, job descriptions, meeting summaries, etc. Generating new content is the classic space that the technology was designed for and will thrive in.


Now, you might be ready to dive into evaluating what makes the most sense. Here is a long list of possible social sector use cases, organized by typical social impact organization departments and the type of Generative AI used. Bring your team together to read through the list, collaboratively flagging any tasks that you see as potentially “high impact” and “low risk.”: 




| Type | Department | Task |
| --- | --- | --- |
| Generate | Programs | Draft program updates and delivery plans |
| Generate | Fundraising | Create fundraising marketing documents |
| Generate | Grants | Draft donor reports |
| Generate | Communications | Create communication materials (docs, image, videos, social media content, etc.) |
| Generate | Fundraising | Proposal notes |
| Generate | Legal | Contract drafts |
| Generate | Operations | Note taking (i.e. for video calls) |
| Generate | Technology | Computer code |
| Generate | Human resources | Job descriptions |
| Generate | Programs | Strategic plans for program implementation based on needs |
| Generate | All | Insights and advice in specific situations of crises |
| Generate | All | Personalized learning and guidelines |
| Predict | Programs | Climate events, economic crash or inflation, forced migration, conflict, etc. |
| Automate | Data | Codebooks \& metadata documents |
| Automate | Data | Labeling unlabeled data |
| Automate | Data | Database wrangling, cleaning, and quality checks |
| Automate | Data | Generating data taxonomies |
| Analyze | Evaluation | Project evaluation |
| Analyze | All | Sentiment analysis |
| Analyze | Human resources | Impact \& performance |
| Detect | Programs | Natural disasters and anomalies |
| Detect | Technology | Fraud |
| Detect | Technology | Mis and disinformation |
| Review | Technology | Review computer code to find bugs or mistakes |
| Review | All | Find errors or trends within documents |
| Review | Human resources | Review candidates fit with job description |
| Summarize | Research | Rapid research synthesis |
| Summarize | Research | Summarize research findings and reports (analyze patterns in large sets of reports and identify trends) |
| Summarize | Evaluation | Summarize impact reports |
| Summarize | Fundraising | Summarize available funding and resources |
| Summarize | Operations | Summarize meeting notes |
| Summarize | Operations | Summarize videos or audio |
| Manage | Operations | Organize notes |
| Manage | Evaluation | Identify and organize themes within qualitative data |
| Manage | All | Classify information |
| Generate | Communications | Design presentations, storyboards, etc. |
| Generate | Communications | Edit images \& videos |
| Analyze | Data | Image tagging |
| Generate | Data | Layout designs for visual data |
| Generate | Operations | Creating templates |
| Generate | Communications | Creating talking points |
| Generate | Communications | Formatting documents |
| Generate | Operations | Creating checklists or task lists |
| Analyze | Grants | Matching SDGs to outcomes |
| Analyze | Operations | Responding to audits |
| Analyze | Grants | Automatic report tagging |
| Analyze | Operations | Semantic search, searchable knowledge |
| Manage | Programs | Personalizing the service delivery experience with chatbots |


Evaluate these opportunities, and any others you can think of, in order to identify and prioritize relevant use cases to define a vision and to find focus. Visit the projects section of the DataKind Playbook and dive into the “[Design Stage](https://datakind.github.io/design.html)” for resources on opportunity identification, the project design process, and narrowing your use case. Follow design thinking principles to co\-create with communities impacted, discuss the most urgent problems, and identify where GenAI might create the most value.


##### Risks Evaluation and Mitigation


Next, consider challenges, constraints, and guardrails for risk mitigation for any possible use cases. For comprehensive risk management, consider all four steps of a [standard risk assessment approach](https://www.iso.org/iso-31000-risk-management.html): (1\) Risk Identification, (2\) Risk Analysis, (3\) Risk Evaluation, and (4\) Risk Treatment. For the purpose of this Playbook article, we are just focused on sufficient high level risk evaluation and mitigation strategies to inform selecting a use case and scoping a GenAI project. Holistic risk management comes later on, after a use case has been identified with risks in mind.


There are so many risks that we need to be aware of when we start to think about using GenAI. We’ve broken them down into five broad categories.


1. **Hallucination** \- or inaccuracy \- one of the most crucial blockers to many use cases is that GenAI can provide plausible\-looking responses which are factually incorrect.
2. **Bias** \- a really big category that encompasses many limitations and areas of concern, this includes the fact that the model surfaces bias and prejudice as found on the internet. Additionally, the GenAI tools can be inaccessible or not inclusive across languages (for example) and other human differences, increasing inequity.
3. **Transparency** \- commercial models are usually closed access. This means that you cannot know what data the model is being trained on and how it works, which is very dangerous.
4. **Misuse** \- there are so many ways GenAI can be misused. For example, data leakage means that private data someone might share with an LLM may be used or exposed elsewhere. We’ve been hearing a lot about dangerous and harmful deep fakes, which is when someone modifies real content to deceive. And, even when guardrails are in place, bad actors can attempt prompt injection to jailbreak from the guardrails and exploit the model for any nefarious purpose, such as producing hate speech.
5. **Development** \- the substantial computing power of these models can have a large environmental impact, there is risk of worker exploitation involved in the humans needed to test and train the model, and there is a large risk of intellectual infringement resulting in plagiarism when the model is trained on words and images created by a human without their explicit consent or usage rights.


In addition to the policy development step mentioned in the article “[Getting Started with GenAI](https://datakind.github.io/genai.html),” one of our first mitigation strategies is to scope and select a problem with the risks top of mind. It is essential to start with a very narrow and low risk use case, as this helps the LLM to maximize safety and minimize risks of harm.


On top of careful scoping to select a safer use case and general policies to mitigate risk across all GenAI use, it’s important to define specific criteria and solutions to ensure safety, accountability, and equity are built into the use case you select. The table below provides sample solutions to implement to mitigate risks for a use case. Please note it is nowhere near comprehensive; rather, it is meant to give you a solid starting point for how to think about risk mitigation in this space. 




| Sample area(s) of risk | Sample mitigation approach(es) |
| --- | --- |
| Hallucination, information loss, errors | * Tools for controlling LLM outputs: [Guardrails](https://www.guardrailsai.com/), [Outlines](https://outlines-dev.github.io/outlines/), [LMQL](https://lmql.ai/), and [SGLang](https://arxiv.org/pdf/2312.07104.pdf). * Inference strategies to generate better outputs using calls to models and tools: [chain\-of\-thought](https://arxiv.org/pdf/2201.11903.pdf), [self\-consistency](https://arxiv.org/pdf/2203.11171.pdf), [WikiChat](https://arxiv.org/pdf/2305.14292.pdf), automated validation techniques like [RAG](https://arxiv.org/pdf/2005.11401.pdf) * Less technical elements: limit data sources and always include references for required human\-in\-the\-loop fact checking reviews |
| Data leakage | Data security systems, select a tool that protects privacy |
| Misuse, [Jailbreak](https://chats-lab.github.io/persuasive_jailbreaker/), model exploitation, prompt injection (i.e. [a worm that targets GenAI applications such as RAG systems](https://sites.google.com/view/compromptmized)) | * Setup model safety guardrails and build in accountability with observability, monitoring, red teaming, etc. to ensure model compliance and appropriate responses to harmful requests * Use the [same care as with the installation of other software and libraries with open models](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) |
| Bias | Test for equity and inclusivity for historically disadvantaged communities |
| Transparency | Select a constrained use case for clarity into how it’s working |
| Inaccessibility (language, internet access, etc.) | Include translation checks, create accommodations to increase accessibility, etc. |
| Carbon footprint/climate change | Conduct cost\-benefit analysis to help select cases and approaches to minimize computing power used |


It’s important to note that although GenAI is very easy for anyone to use, there is a learning curve to ensuring safety by design. Using these tools responsibly requires an investment of time to develop staff skills, implement these solutions, and continuously test and monitor. 


Pulling it all together, here’s an [example of what this AI risk evaluation looks like](https://docs.google.com/spreadsheets/d/1sM_TKqu5zmazZGtNvkwSvHSmXDZZeXV8/edit#gid=1135542121) in The Wildlife Trusts’ effort led by Alice Kershaw. They have generously shared their working draft built with DataKind volunteer Daniel Nissani after participating in a [DataKind Learning Circle](https://www.datakind.org/2023/10/17/introducing-datakind-learning-circles/), so that you can see a real life example of how this might play out in your social impact organization. Find more examples in the [GenAI Resource Hub](https://datakind.github.io/resource_hub_for_genAI_in_the_social_sector.html). 


##### Making a decision


Focus on identifying and building low risk solutions, while mitigating any remaining risks. For example, asking an LLM questions where the answers are from its training data is high risk, with a large possibility that it will provide false information. Whereas, using an LLM to predict technical metadata on data you provided is a more low risk solution. While low risk solutions are still not risk\-free and require mitigation strategies, they are much better places to start. Assess the risks and possibilities across use cases, using a simply matrix: 



![](/public/img/genAI_risk_Picture1.png)

When selecting your GenAI problem statement, use this matrix to evaluate risk (the x\-axis) versus impact (the y\-axis). Think about where any possible GenAI use case might fall. You are looking for a use case that falls in the top left quadrant, with the lowest levels of risks and the highest possible impact. Think through possible use cases, assess the risks for each opportunity, and chart them on this matrix to identify what would be the best place to start. 


For example, see the table below for examples of risk and guardrails specific to a few program evaluation and impact assessment use cases: 




| Use case/opportunity | Area(s) of risk | Mitigation approach(es) |
| --- | --- | --- |
| Summarize research findings and reports (analyze patterns in large sets of reports and identify trends) | Summaries reflecting demographic biases and inaccuracies from low quality inputs. | Implement bias testing. Follow [ethical data practices](https://datakind.github.io/). Use quality filters for input sources. Account for language/cultural nuances. |
| Sentiment analysis (clustering responses to a positive, negative or neutral sentiment depending on the text using natural language processing) | Biases in training data leading to inaccurate sentiment analysis across demographics. | Periodically validate sentiment analysis results against human judgments and adjust models accordingly. |
| Conduct analysis for project evaluation | Hallucination, security, overreliance: Potential biases in evaluation processes and decision\-making rationale lacking transparency. | Regularly validate project evaluations. Include reasons behind decisions for transparency. Analyze data and "score" using different weights to determine confidence levels. |
| Identify and organize themes within qualitative data | Omission of key perspectives across diverse contexts in identified themes. Data security. | Validate AI\-identified themes against human judgment. Provide clear security controls for any sensitive qualitative data. |


This about how harmful the risk is, beneficial the use case is, and feasible the mitigation approach identified is. Creating a table like the one above to unpack the use cases you are considering will help you prioritize and select a starting use case. 


Please see other "scoping" articles for social impact organizations, just like seen at the bottom of the page here: <https://datakind.github.io/scoping.html>