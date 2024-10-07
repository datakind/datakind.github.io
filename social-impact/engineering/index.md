---
layout: page
title: Where to Start with Data Engineering
subtitle:
date: 02/29/2024
author: Chip Felton, Shouvik Basak, Matthew Hutchinson, Sridhar Ganapathy, Colleen Rosales, Fotis Zapantis, Jay Patel, Michelle Maluwetig, Sarah Lenet
audience: DataKind Volunteers
category: social-impact
subcategory: engineering
articles:
  - title: "Identifying & Scoping an Equitable Data Project"
    filename: "identifying_scoping_an_equitable_data_project"
    date: "March 28, 2024"
    author: "Caitlin Augustin"
    handle: "augustincaitlin"
---

Data engineering is an important and overlooked element of using data at social impact organizations (SIOs), required by many data projects to set up or sustain any large scale data work. There’s lots of information available on data engineering, so rather than creating something from scratch, this Playbook article compiles and organizes resources that might be useful for SIOs looking to improve their data infrastructure, answering a few frequently asked questions by pointing you to relevant resources to learn more. 


**How can my organization get started with our first data pipeline?**


Start with [this introductory webinar](https://www.youtube.com/watch?v=AD4hO3apBJk&list=PLatLcguzOb4HALE61UGWZaTwWzmD_k5xE&index=2), meant to familiarize you with the concepts of data engineering and infrastructure (i.e. defining concepts like “data pipeline” and “ETL (Extract, Transform, and Load)”) and provide insight into how to get started at your organization. You can also [review the slides](https://drive.google.com/file/d/1MaHAnyLTHdXtLvNeel71H9ST4AdFoHh3/view?usp=sharing) to find example pipelines, definitions, and nonprofit sample data engineering projects and workflows.


Then, these resources below are for SIO professionals looking to get started with building data pipelines and setting up a data infrastructure for their organization.


**Google Sheets:** For a smaller organization with limited data and/or skills on staff, Google Sheets might be a good starting point for your data infrastructure needs. Most tools nonprofits might use (*such as survey collection tools like ODK, event software like Zoom, or email marketing like Mailchimp*) integrate with or export to google sheets, and it’s free. By moving data from existing software to google sheets for analysis, and then pulling data from google sheets for use, you can experience your first example of what a simple data pipeline could do for your organization. Here’s [a demo](https://docs.google.com/spreadsheets/d/1-pHlFEUQ0E2f8HWM4zokdmQN7MEcptkVPMyaqdcIQqs/edit#gid=0) of some of the most useful functions in Sheets from a data pipeline perspective. [Apps Script](https://developers.google.com/sheets) can help write custom functions, automate tasks, create visualizations, add menus/sidebars on Sheets using Javascript.


**Business Intelligence (BI) Tools:** For setting up a classic data engineering pipeline at entry level, it might work to use a BI tool, such as Power BI dataflows or Tableau data prep. The modern BI platforms can work as engineering pipelines, and there are organizations that do all their engineering like this. It's not for everyone, but a nice example of cleaning, processing, normalizing and modeling data with an easy\-to\-use interface. Entry level orgs will be able to get started with data engineering at quite low cost.


**Ready to start to map out your organization’s current architecture and data flow?** [draw.io](https://app.diagrams.net) is a great, free platform for diagramming workflows, databases, data/software architectures, etc.


**What data engineering software options are available with discounts for social impact organizations?** 




| Software | What it provides | Discount for SIOs |
| --- | --- | --- |
| AWS | [AWS for Nonprofits](https://aws.amazon.com/government-education/nonprofits/?wwps-cards.sort-by=item.additionalFields.sortDate&wwps-cards.sort-order=desc) provides computing power and storage through relational databases. | Through the [AWS Nonprofit Credit Program](https://aws.amazon.com/government-education/nonprofits/nonprofit-credit-program/), eligible nonprofits and public sector organizations can get AWS Promotional Credit (amount depends on size), helping to offset costs associated with implementing cloud\-based solutions. AWS also has a [free tier](https://aws.amazon.com/free/?trk=b53e5260-30f6-45cf-9610-30be63969231&sc_channel=ps&s_kwcid=AL!4422!3!610000101498!p!!g!!aws%20server&ef_id=Cj0KCQjwk7ugBhDIARIsAGuvgPbYRv9biMyWtJjb_2dtgnWXbTwEttm4p7hgk6A6yClTfV5FTrVD5csaAjypEALw_wcB:G:s&s_kwcid=AL!4422!3!610000101498!p!!g!!aws%20server&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) with many resources available at no cost, regardless of eligibility. |
| Salesforce | [Salesforce for Nonprofits](https://www.salesforce.org/nonprofit/) offers CRM software for nonprofits that connects all your organization's functions across fundraising, marketing, program management, grant making, and operations. | Through the [Power of Us Program](https://www.salesforce.org/power-of-us/), eligible nonprofits and educational institutions get ten free subscriptions to Salesforce and deep discounts on additional subscriptions, products, and/or services from Salesforce. |
| Splunk | Splunk is a data infrastructure tool that provides a secure, reliable, and accessible platform for your organization's data. | Splunk provides a one\-year, 10GB license for Splunk software to all qualifying nonprofits at no cost, as well as complimentary e\-learning and support to get you started, through their [Splunk Global Impact Donation Program](https://www.splunk.com/en_us/about-us/splunk-pledge/nonprofit-license-application.html). |
| Tableau | Tableau offers easy\-to\-use desktop and web\-based software for data visualization, data analysis and data preparation. | Nonprofits can request donated Tableau Desktop licenses [Tableau for Nonprofits program](https://www.tableau.com/foundation/license-donations). |
| Google | [Google for Nonprofits](https://www.google.com/nonprofits/) offers eligible organizations access to Google products and discounts that can help solve the challenges nonprofits face: finding new donors and volunteers, working more efficiently, and getting supporters to take action. | Google for Nonprofits provides access to many Google products. Make sure to [check to see which Google for Nonprofits' products are available in your country](https://support.google.com/nonprofits/answer/1614602). Additionally, Google Cloud Free tier enables new Google Cloud users to take advantage of a 90\-day trial period that includes some free Cloud Billing credits, covering several storage and compute products. |
| Microsoft 365 | [Microsoft 365 for nonprofits](https://www.microsoft.com/en-us/microsoft-365/nonprofit) offer office tools and cloud solutions like Azure, Dynamics 365 and Microsoft 365, as well as nonprofit\-specific software for fundraising and engagement. | [Microsoft 365 for nonprofits](https://www.microsoft.com/en-us/microsoft-365/nonprofit) provides grants and discounts to eligible nonprofits around the world; [initial registration is required](https://nonprofit.microsoft.com/register). After eligibility validation and notification, the organization receives an email with details on how to access the grants and discounts. More details can be found [here](https://www.microsoft.com/en-us/nonprofits/faq?rtc=1). They also offer webinars on nonprofit topics such as fundraising and donor retention. |
| Observable | [Observable](https://observablehq.com/about) is an end\-to\-end tool for building data apps, creating data visualizations, hosting data projects teams, and learning in community. | Observable offers discounts for educators and nonprofits, [contact their sales department](sales@observablehq.com) for more information. Most notebook features are available with the free tier; see the [pricing page](https://observablehq.com/pricing) for detailed information. |
| Airtable | [Airtable](https://www.airtable.com/product) is a spreadsheet\-database hybrid and a great next step for those familiar with Excel or Sheets, as it provides a low/no\-code route to creating simple data pipelines: start with data collection interfaces (forms), process data as you would in spreadsheets, and search/ visualize/ summarize your data. | Airtable offers a [50% discount for nonprofits](https://airtable.com/shr9DxhP6lU9slZE6). |
| Apache Airflow | [Apache Airflow](https://airflow.apache.org/) requires knowledge of python to use for developing pipelines, but provides all the functionality of a commercial ETL platform for free. | Apache airflow is entirely free and open source! |


For more, [TechSoup](https://www.techsoup.org/) compiles and helps organizations access discounted and free software and services for nonprofits. You can also find access to data and AI guidance through free resources for nonprofits: [Tekalo](https://www.tekalo.org/sign-up/organizations) (to hire technical talent) and [Catchafire](https://www.catchafire.org/causes) (to work with volunteers).


**How do I connect the software to build an entire pipeline from source to deployment?**  

 Connecting this back to the [pipeline examples](https://drive.google.com/file/d/1MaHAnyLTHdXtLvNeel71H9ST4AdFoHh3/view?usp=sharing), a commercial ETL platform will help orchestrate tasks in a chronological order with dependencies. You can schedule runs of your code or pipelines at specific times. Alongside this, Continuous Integration and Continuous Delivery (CI/CD) tools such as Jenkins ensure the codebase is functional at any time and that code can be released without manual intervention. Event hubs, such as Kafka, enable you to create message queues and topics to send data to specific services, catch errors more easily, and offer many other advantages.


I’d like to select a database platform. Where should I start?  

 If you’re ready to move towards more advanced data management, it might make sense to learn and use relational database management system software.


First, you may want to learn SQL using a free tutorial like [Code Academy](https://www.codecademy.com/courses/learn-sql/lessons/manipulation/exercises/sql) or [W3](https://www.w3schools.com/sql/), if you haven’t already.


Then, consider the following options:


* [PostgreSQL](https://www.postgresql.org/): A free to use, full\-function relational database platform that provides everything you could need to support a relational data model, including full text searching, recursive queries, storing and querying GIS and JSON data, graphical and cli tools, as well as sophisticated performance tuning and memory management functionality.
* [MySQL](https://www.mysql.com/): A commonly used ‘freemium’ database platform owned by Oracle, limited in functionality without purchase of OracleDB.
* [MariaDB](https://mariadb.org/): A more lightweight platform than Postgres, but it is truly open source and completely free to use. It also comes pre\-installed in most linux distros so can be a good starting point for simple databases.
* [Neo4j](https://github.com/neo4j/neo4j): The leading graph database engine, a great fit for small teams working with networked data. It’s free to use but not open source and some functionality like HA clustering is restricted to the paid version.
* [Observable](https://observablehq.com/@observablehq/working-with-sql): Query SQL directly from a notebook by either (1\) the SQL cell provides an interface for writing SQL queries and viewing the results, as well as inspecting the schema of the tables in a database, or (2\) the Observable framework includes built\-in support for client\-side SQL powered by DuckDB.


If you don’t want to learn SQL and would prefer to use JSON\-like documents, consider:


* [Couchbase](https://www.couchbase.com/products/server/): A NoSQL database well fit for time series and very fast read and write operations.
* [MongoDB](https://www.mongodb.com/): A NoSQL database with its specific querying language, powerful and popular, but can be difficult to get onboarded.


Finally, if you’re looking for funding for your data infrastructure project, [Invest in Open](https://investinopen.org/blog/exploring-funding-for-open-infrastructure-services-preliminary-observations-and-next-steps/) provides information on funding for open infrastructure services.


**I’d like to dive more into learning about data engineering and infrastructure. What do you recommend?**


Start your journey with a book: [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) by Joe Reis and Matt Housley (O’Reilly). This book is a good reference on how to plan and build systems to serve the needs of the organization, by evaluating the best technologies available through the framework of the data engineering lifecycle. This book will help to:


* Get a concise overview of the entire data engineering landscape
* Assess data engineering problems using an end\-to\-end framework of best practices
* Cut through marketing hype when choosing data technologies, architecture, and processes
* Use the data engineering lifecycle to design and build a robust architecture
* Incorporate data governance and security across the data engineering lifecycle


Please see other "scoping" articles for social impact organizations, just like seen at the bottom of the page here: <https://datakind.github.io/scoping.html>