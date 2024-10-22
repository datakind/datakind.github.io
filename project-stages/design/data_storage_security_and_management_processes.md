---
layout: default
title: Data Storage, Security, and Management Processes
date: 02/29/2024
author: Benjamin Kinsella, DKSF Chapter, Jeremy Osborn, Lawrence Kilroy, William Ratcliff, Dulcie Vousden, Rachel Wells, Edwin Zhang
audience: DataKind Volunteers
category: project-stages
subcategory: design
---
Once you have signed contracts, you are ready to start working with the partner organization’s data! ata security and privacy are critical components to any data science project. Using the process below will help you understand how to identify, access, transfer, store, and/or dispose of sensitive data, so that we can appropriately manage data throughout the project process to mitigate risk and build trust with partners. DataKind is [GDPR compliant](https://gdpr.eu/), but more importantly, DataKind cares about protecting people's privacy to ensure our work remains in alignment with our values. For a full summary of DataKind’s data security standards and policies, see [this slide deck](https://drive.google.com/file/d/19H5Oeyfut1enu2H4v7-lw6MFQ0IpOznk/view).


It is essential that you understand your responsibility to identify data security and privacy requirements, and conduct risk mitigation before executing your project. Identify potential unintended consequences from transfer of data as you move through this process, and be prepared to audit and document the processes you execute with respect to the data as well as who had access to the data and when that took place.


Below is our process for data storage, security, and management at DataKind:


1. Send the partner organization the  [Data Security Questionnaire](https://docs.google.com/forms/d/1KXh9JnHKtAlrR6wUDNPYFODeDEgg94UahEPAE3t7i7o/edit) (using  [this link](https://docs.google.com/forms/d/e/1FAIpQLSfeUISdh2uvLQXWnp4AWNj51ERH8-_Hx_S8ATzJJ2iDaPqwIA/viewform)). The questionnaire aims to capture the organization’s data and their sensitivity, in addition to potential legal requirements and governance.
2. Reach out to your DataKind staff support, and they will send you the answers to the Data Security Questionnaire for your partner organization.
3. Use the  [DataKind Classification](https://drive.google.com/file/d/11sfuF1sDjFCa2-DbTGaArs8KJK3mhmN3/view) to classify the partner organization based on their responses within the questionnaire.
4. Create a  [Data Management Plan](https://docs.google.com/document/d/12U4ptw1EGIzc2T2LzT1jOLQD51Q-qJj4JfIhMLt5iHw/edit) based on the classification.
5. Confirm the plan with the partner organization on a call.
6. Prepare the tools for managing the data according to the plan.
7. Ensure all volunteers on the project have seen the Data Management Plan and are prepared to comply with it.


##### Does DataKind access regulated data and/or data with personally\-identifiable information?


In the vast majority of cases, we only work with projects that do not require the use of any regulated data or  [personally\-identifiable information (PII)](https://en.wikipedia.org/wiki/Personal_data). We care deeply about protecting people’s privacy and have found that it is not necessary for us to access PII to build valuable products for our partners. Additionally, complying with a variety of data regulations requires making significant technical and organizational investments and involves taking on significant legal liability, which doesn’t make sense for us in most cases.


##### What measures and precautions should be taken when working with PII or regulated data?


In the rare cases in which we work with PII or regulated data, we take extra security measures into account. We either work within the partner organization’s compliant system, and/or anonymize the data to the point where it’s no longer covered by the law and contains no PII. De\-identification of PII should be done by the partner organization in advance of transferring the data to DataKind; this is not a responsibility for volunteers at DataKind. If the partner organization needs help with de\-identifying data, work with your DataKind staff support to identify the right person to provide this support before any data is shared. 


Keep in mind that data security and anonymization are not skills all partner organizations have in house. It is up to you to call out data that could be misused or might render people unsafe. DataKind will do everything we can to anonymize data with folks and ensure they are set up for success in anonymizing the datasets. In all circumstances, think about considerations that could leave people vulnerable, such as whether there are so few people in certain neighborhoods that they could be de\-anonymized. 


##### What data should the partner organization share with DataKind?


We practice data minimization at DataKind: partner organizations should only provide access to data that you know could be valuable to complete the project. 


##### Who should host the data in the platform for sharing?


In most cases, it is our preference for the partner organization to host the data themselves and simply provide the DataKind volunteers with temporary access to the data within their systems. This approach better enables long\-term sustainability and minimizes risks for both volunteers and partner organizations. Partner organizations should plan to host and pay for any computing costs. 


##### What’s the default option for managing data in DataKind’s systems?


We generally use Google Drive for management of most non\-highly\-sensitive datasets. Google Drive is both secure (only people on the access control list have access to the data and it’s encrypted at rest), and easy to use for partner organizations and volunteers. If the data is too large for that platform, we often use Amazon S3\. Highly sensitive datasets are generally stored in a secure remote system. That said, if a partner is more comfortable with a different storage solution (such as DropBox), we can work within their preferences for data access, as long as it aligns with the security requirements. 


##### What happens if we are sharing data across borders?


DataKind uses the tool  [OneTrust Data Guidance](https://www.dataguidance.com/) to understand all concerns for data security internationally. Through this tool, we get bi\-weekly updates on relevant international regulations and have on\-the\-ground legal support as needed. We create a workspace for every project within OneTrust, directed to the project’s Data Ambassador, so they receive initial information on the requirements and continuous follow\-up throughout the project.


##### How do I check if data was collected legally?


Make sure you are confident that data was collected without any legal infringement or ethical concerns. This is especially important for user data and any third party data acquisition, such as data that was scraped. If you are unsure whether data was collected legally or if DataKind should have access to it, talk through the situation with DataKind staff. In some cases, we will elevate the challenge to engage a legal team to make sure we are properly supported. We know data scientists are not lawyers, and we don't expect you to be, but we do expect you to ask questions if you are unsure.


##### How does DataKind respond if there is a potential data incident?


We use our [Data Incident Response Checklist](https://drive.google.com/file/d/1TXnkrIt8lEDFydozdlpM1r4PkKejCgxF/view?usp=sharing) if there is ever a potential data incident.


##### What should I do if I have more questions?


If you have specific questions or concerns, know who to turn to for help:


* For technology support and general legal advice, ask DataKind staff. If you’re not sure, always ask the question.
* For general questions, DataKind community members are a great resource! Be mindful, however, not to expose sensitive information on partner organization data.


If you’d like more information on DataKind’s data security processes, you can find it in [this folder](https://drive.google.com/drive/folders/1jFCIiYytn_JTMUx5sKiAh3w1acLxVbkB). Please know that comments are always welcome into any of our processes and documentation, as we are on a journey aiming for continuous improvement.