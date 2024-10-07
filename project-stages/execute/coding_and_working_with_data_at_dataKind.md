---
layout: default
title: Coding and Working with Data at DataKind
date: 02/29/2024
author: Shahab Arabshahi, Benjamin Kinsella, Tyler Dorland, Neal Fultz, Kavita Maheshwari, Michael Dowd, Daniel Nissani, Rachel Wells
audience: DataKind Volunteers
category: project-stages
subcategory: execute
---

##### Working with Data


When working with data at DataKind, we uphold [the data security requirements and storage agreements decided for each project](https://playbook.datakind.org/playbook/articles/31/data-storage-security-management). For example, some projects request that you save data directly on your local computer, while other projects require you to keep the data in the cloud environment and work with it from there, never downloading it to your local computer. Whatever the specific requirements are for your project, we are [GDPR compliant at DataKind](https://gdpr.eu/) , so treat data carefully and maintain data security at all times.


As a general best practice, don’t store data on GitHub or check data into git. Instead,


* Add data formats to data/.gitignore
* Share all data via Google Drive
* Sync data from Google Drive or load directly


(For more on DataKind's GitHub Workflow, see [this article](https://playbook.datakind.org/playbook/articles/205).)


If you are ever unclear about an expectation around data, don’t be afraid to ask! 


##### Coding


When coding at DataKind, we build a culture of code review within the project team because little bugs always just happen! It’s also a great way to include more volunteers. As a data scientist, we expect you probably have a grasp of some coding best practices, but we would be remiss to not mention a few essential coding best practices to keep in mind:


* Always keep a log.
* Follow [best practices](https://ropensci-archive.github.io/reproducibility-guide/) to ensure code reproducibility. To help, we've created a GitHub actions template, which you can use to easily set up a new DataKind GitHub repo (more info [here](https://playbook.datakind.org/playbook/articles/194/using-github-to-set-up-your-datakind-project)). We also have a standard DataKind GitHub Workflow, which you can find in [this Playbook article](https://playbook.datakind.org/playbook/articles/205).
* Never hard code values.
* Write clear, concise comments, including input and return output types for each function you use.
* Document how you handle edge cases and outliers. Never delete data without commenting why.
* Don’t forget to include prerequisite software installation commands in your code.
* Print the time taken by each function and the entire code, including important lines like data inserting or pre\-processing if the functions don't exist. In notebooks, it is recommended to use a plugin (for example, [this one](https://stackoverflow.com/questions/56843745/automatic-cell-execution-timing-in-jupyter-lab)).
* For software development projects, make sure the test cases exist (APIs, DB querying, get and put requests).
* Secure all http requests.
* If you have a server receiving data from external users, use the query parameters built into every database drive to ensure the content conforms to allowed values to avoid SQL injection attacks.
* Most projects will need a license. The [MIT license](https://opensource.org/licenses/MIT) is a good default if you're not sure what to use.


##### Open Sourcing \- Python Code Consistency


Effective coding collaboration is enabled by sharing code that has been developed to a standard quality. However, the standard should not be too aggressive as to impede progress. To this end, we use two tools as described [here](https://towardsdatascience.com/keep-your-code-clean-using-black-pylint-git-hooks-pre-commit-baf6991f7376).


1. The [formulaic python formatter “black”](https://pypi.org/project/black/). As described by its authors it is deterministic and fast, but can be modified. We use the default settings, most notably formatting to a character limit of 88 per line.
2. The [code linter pylint](https://pylint.org/). This follows the [PEP8 style standard](https://peps.python.org/pep-0008/). PEP8 formatting standards are taken care of in black, with the exception that the default pylint line length is 80\. Pylint is also modifiable and a standard set of exclusions to the PEP8 standard we have chosen are found [here](https://github.com/datakind/medic_data_integrity/blob/main/.pylintrc). We chose the default score of 7 as the minimum score for pylint to be shared.


The combination of black and [pylint](https://example.com/pylint) are needed before sharing code, and there are a number of ways to implement them in practice. Many common IDEs like [VSCode](https://code.visualstudio.com/docs/python/editing#_general-formatting-settings) and [PyCharm](https://plugins.jetbrains.com/plugin/11084-pylint) have settings or plugins for the packages. They can be incorporated into the git process using a pre\-commit hook as described in the first resource. An optional slightly modified setup script for the pre\-commit hook can be found [here](https://github.com/datakind/medic_data_integrity/blob/main/setup_hooks.sh).


Finally, no guidelines for coding consistency would be complete without unit tests. As many different styles of unit testing exist, we don’t make specific recommendations on the type or style of unit tests, but we do recommend using them in the [pytest](https://pytest.org/) framework.