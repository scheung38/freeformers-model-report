## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

You are given a CSV file containing results from an online evaluation tool, giving users a score for some of the attributes they were evaluated against. Participants can take the survey any number of times before, during, and after following a series of online lessons. We would like to test the efficacy of those lessons in improving participants’ results to this evaluation.

Your task is to write a program that compiles an improvement report out of those scores. The report should show, in a machine-readable format of your choice, the average improvement made by our participants for each attribute in the set.

The CSV file is chronologically sorted, items at the bottom are more recent than items at the top. For example, given this CSV file:

user_id,area,attribute,grade

8,technology,forward_thinking,63

8,technology,forward_thinking,67

9,technology,forward_thinking,70

9,technology,forward_thinking,70

User number 8 improved their score in the forward_thinking attribute by a total of 4. User number 9 did not improve their score. The average improvement for all users on this attribute is 2. A sample output for this CSV input could be:

area,       attribute,          average_improvement
technology, forward_thinking,   2

● How to run your solution and get the report.

● How to run the automated tests for your project, if any.

● Any technological choices you made during the exercise, if any.

● Any assumptions you made during the exercise, if any.

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.
Solution uses Pandas and Numpy package for Python for data manipulation for the above coding challenge
The automated tests for the project uses travisCI build that checks for the

/test/modelReport_test.py upon every push into GitHub repo by automatically launching

$ pytest

Assumption is that this csv is to be executed on a local machine, no attempt was made to fully launched into distributed remote
clusters of machines to optimize performance.



## Installation

Provide code examples and explanations of how to get the project.
$ pip install -r requirements.txt

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests
$ cd test/

Describe and show how to run the tests with code examples.

$ pytest

## Contributors
Zahara Miriam

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)