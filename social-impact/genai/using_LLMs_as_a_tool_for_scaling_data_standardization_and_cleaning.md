---
layout: default
title: Using LLMs as a Tool for Scaling Data Standardization and Cleaning
subtitle: This article contains pointers for anyone looking to adopt LLMs for data standardization and cleaning tasks. It is a deeper dive into the technical details of one use case, intended for a user that is experimenting with Generative AI.
date: 02/29/2024
author: Deborshi Goswami with Jacob Leppek and Rachel Wells
audience: Social Impact Professionals
category: social-impact
subcategory: genai
---

This article came from a collaboration between DataKind volunteer Deborshi Goswami and Vivery. Onboarding new partners into the Vivery platform requires a lengthy data collection, cleaning, and standardization process. Since each partner stores data in different formats, a “if\-then” rules\-based parsing approach isn’t flexible enough to work across multiple partners. LLMs can assist with the cleaning and standardization process with messy data that isn’t consistent in its formatting.


For example, imagine you are trying to parse open hours from a string: one user may have described an open time as “1st Tuesday 9:30\-4”, and another user might have written “Tues 9:30 \- 16:00 (1st only)”. While you might need to write multiple regular expressions to capture all of the pattern occurrences, a LLM offers a more flexible approach that can accommodate both options, recognizing that the same information is encoded in the string. By fine\-tuning or giving the LLM instructions on how to format its output, it could return “1st Tuesday 9:30 AM \- 4:00 PM” for both examples, creating a database\-friendly output.


However, a successful application of LLMs in this context only works if you are continuously validating the performance and refining the methodology. The following tips might be useful for anyone working on a similar use case.


On testing the methodology at large:


* Think about outcomes in an iterative manner. Facing issues with prompt engineering and response quality are quite normal. It is a process of systematically and incrementally improving the system to converge on the best outcome over time.
* Adopt an experimental approach to the problem which consists of cycles of thinking about which part of the system is not optimal, trying out an experiment to improve it, and evaluating the results. It is totally okay if this is a slow process that improves over time.
* Have extensive testing functions to programmatically validate the format of the outputs. If we expect **HH:MM AM TZ**, as the output format then we can write regex based unit\-tests to validate that.


On validating whether the output of the LLM actually corresponds to the input:


* Manually validating a sample and implementing the experimentation strategy mentioned above before using prompts is important. This is both the most accurate and simultaneously the most painstaking way.
* If you wish to be programmatic about it, try an LLM\-based method where you ask the LLM to evaluate the response for you. The prompt can be something like: "The following is a query\-response pair, where the query is unclean user inputs and response is a cleaned \& standardized version of the input. Tell me whether the response truly is a standardized version of the input or if there are inaccuracies in the output. Answer only yes or no."
* You can also give the prompt some one\-shot examples of this task.
* When the LLM says it is an invalid output, maybe then you can intervene. There is a likelihood of False Positives and False Negatives with this method, but as long as you are identifying most inaccuracies, that's a much better place to be in.


On fine\-tuning vs prompt engineering:


* If you can find solid examples of invalid responses from the above method, you can fine\-tune the model by correcting them.
* However, I would also recommend giving a thorough look into prompt engineering (here is [a guide](https://www.promptingguide.ai/)). It's an iterative process and doesn't always land the first time, but there are many powerful ways in which you can provide guardrails to your LLM for more accurate results. These include:
	+ One\-shot examples: Give examples of what successful input\-output pairs look like
	+ Chain\-of\-Thought Prompting: Give examples to the LLM on how to reason why 930a maps to 9:30 AM, and also ask the LLM to reason their answers, we find that reasoning through a problem helps LLMs give better results.
	+ Prompt Chaining: Chain prompts one after the other to fine\-tune the result if needed, for example, "give standardized output for this input" followed by "is this output correct for the given input" followed by "improve the output to correctly match the given input"
* Check [this resource](https://www.guardrailsai.com/docs) for more sophisticated methods of providing guardrails to your LLMs.


On hallucinations:


* Again, manual validation is key here, but one parameter to play with, if you don't already, is the temperature of the model. Lower temperature means less creativity, but also less likely to hallucinate.
* There are prompt\-based ways to mitigate hallucinations, for example having sentences like: 'if you are unsure, just say "I don't know."’ Here is a [guide with a video](https://medium.com/@masteringllm/6-ways-to-reduce-hallucination-using-prompt-engineering-b30eb244b9b2) that might be helpful.


On getting buy\-in and feedback from stakeholders:


* The most important thing here is to set expectations that improving the accuracy of data is an iterative process, then designing a program around that expectation.
* Enable your stakeholders to review your data and make corrections and design your system such that updates are regular and a central part of your process.
* One tool that might help here is [Argilla](https://argilla.io/), which can be used for making iterative improvements in our chatbots. It's easy to set this up in a way that you can expose LLM outputs to internal and/or external stakeholders and collect feedback.


On iterating vs getting it right the first time:


* Let us say you are having a hard time deciding if it is okay to have some inaccuracies in LLM outputs and how iterative you can afford to be when releasing the data for production, the framework to keep in mind is, "What harm do inaccuracies cause?"
* If responses are hallucinated to the point where they are (this is just an example and quite unlikely for this use\-case) insulting the user, then definitely we need to catch them before pushing to production. But if one of the programs are listed instead of two, then maybe it is okay to update it once the error is caught. It depends on your risk tolerance, what kind of errors you and your stakeholders are okay with, and what the alternative option is (i.e. was the previous version more error prone?).


Please see other "scoping" articles for social impact organizations, just like seen at the bottom of the page here: <https://datakind.github.io/scoping.html>
