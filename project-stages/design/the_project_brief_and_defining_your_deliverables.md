---
layout: default
title: The Project Brief and Defining Your Deliverables
date: 02/29/2024
author: Caitlin Augustin, Mitali Ayyangar, Benjamin Kinsella, Emily Yelverton, Rachel Wells, Caroline Charrow, Nathan Banion, Seward Lee
audience: DataKind Volunteers
category: project-stages
subcategory: design
---

As you plan out your project, you’ll need to explicitly and clearly define the project deliverables. This is a very important step for multiple reasons:


* Prior to execution, it’s important for both DataKind and the Project Champion to decide whether it’s worth moving forward in the partnership. This will be largely informed by the feasibility and expected impact of the deliverables.
* Getting mutual commitment to project deliverables ensures that there’s a clear objective or goal state for the project, and the team knows what they’re working towards. Without clear deliverables, the team may not be building the right solution, and we risk creating a product that provides minimal value to the partner organization.
* Clearly defined deliverables offer protection against project scope creep. It’s hard for volunteers to stay focused and energized when a project has no clear goal, and they’re stuck with fulfilling a continuous stream of unprioritized requests.


Once your deliverables have been defined, you will turn them into a project brief that serves as a shared agreement between DataKind and the partner organization on the project scope, relevant resources available, and each team’s responsibilities. 


##### The Project Brief


* **Template:** This [Project Brief template](https://docs.google.com/document/d/1g4v5_TH8frH6utNoMa0-DY3J4H_ohMKvfszoEPYXaFk/edit?usp=sharing) is meant to be a guideline or example. If it would not be helpful for you to fill in every section, feel free to skip what isn’t valuable for your project. If a section would be helpful that is not included here, feel free to add it. Project Briefs are flexible and meant to document and reflect the specific needs of the project!
* **Who interacts with the Project Brief?**
+ The DataKind Scoper and the Project Champion will co\-create it gradually while discovering and designing the project.
+ The project volunteer team will read it once as part of onboarding.
+ The DataKind Project Manager and the Project Champion will update the document as needed at all check\-ins throughout the project process to maintain a single source of truth about the project.

* **What the Project Brief isn’t**
+ A document outlining the technical project plan. Teams will find these materials in GitHub, asana, or another task management software.
+ A document summarizing why DataKind decided to pursue this project.
+ A document to agree upon language to use externally about the project. This [Project External Messaging Template](https://docs.google.com/document/d/1zM4sdPBG_Hulwm34FOzUQllhSib2OlEOtoieUU5naC4/edit#) can be used by communications, donor relationships, and fundraising teams for both DataKind and the partner organization at any time for that purpose.


**Please keep in mind that this is a potential exit point for both DataKind and the partner organization. At this stage, it’s okay to decide not to pursue a project if we can’t define satisfactory deliverables!** It’s better to pause the relationship and pursue a project at a later date than to go full\-speed ahead to build deliverables that are either poorly\-defined or low\-value. 


##### Frame the Solution


Sometimes we build custom solutions for a partner organization, but sometimes we build solutions that are meant to be generalizable for a greater impact beyond just the partner organization. While being mindful of the tradeoffs, ensure you have clearly identified the primary user of the solution, whether it is the specific partner organization or an entire sector, and define the deliverables accordingly. If the priority is to design a generalizable solution, ensure that is called out in the Project Brief. If the partner organization is not interested in a wider solution, don’t waste time trying to generalize a solution too early. It is often best to start with sticking to the narrow solution unless and until generalizing is your primary objective.


**Tip:** Take advantage of timescales in framing the solution. What could reasonably be accomplished in a six month DataCorps engagement? What incremental deliverables could the team work towards at which point in the project? Is there anything that could be broken out into a possible follow\-up project? 


Regardless of where you land in the tradeoff, it is essential to keep in mind how the partner is going to use the product. For example, don’t spend time designing a pretty web interface to interact with the data, when the partner really needs a model that will integrate with their decision making systems and software. Be clear on the exact deliverables you plan to create, and ensure they will actually be useful to the partner organization!


##### Workstreams


During this process, one approach is to split the project into discrete “Workstreams”. If you choose this approach, be careful to not delve into project management, unless you plan to stay on the project as the Project Manager for executing the project. For each workstream summarize:


1. Key activities involved in the workstream
2. Key deliverables produced by the workstream


For example, in the DataKind San Francisco project with Muso, one of the workstreams was defined in the following manner:



**WORKSTREAM 1:** The DataKind team will create an algorithm using Python which will be used on each new year’s data to assign the Record ID from the prior year. This will allow records across years to be linked.
Key activities for this workstream include:


* Transform data to be standardized
* Iterate through different probabilistic record linkage models
* Choose model which creates valid results


Key deliverables include:


* Instructional resources for transforming data and executing model
* Executable Python code to run on transformed data
* Code will produce a CSV file of the imported data with a new data field which contains the linked records Member ID, or a generated Member ID for new data
* Technical writeup of process to arrive to final model