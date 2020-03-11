# Brown-Bag

This is a compilation of hackathon / interview style questions and problems.
At the root of each directory, I include a markdown file which describes the problem.
Subsequent, language-specific directories contain minimum test cases and my personal implementations of solutions.

Problems often include a time-limit guideline.
The initial challenge is to pass all minimum test cases within the time-limit; however, my posted solutions are often refined beyond the initial time-constraint.

If I have multiple working solutions to a problem, I will comment in their respective asymptotic running-time.

## How to run test cases

Test cases and their respective solutions live as their own module, and should be runnable by navigating to the solution's directory and running the language-specific command as described below.
I have also listed the default version I have used to implement and test each language.

Language   | Version         | Shell Command
---------- | --------------- | -------------
Python 3   | 3.8.x           | `python ./test.py`
JavaScript | Node.js 13.10.x | `node ./test.js`

*Note: Shared code is joined by relative symlinks to the utility file in [`./utils`](./utils).
If these symlinks give you trouble, you can always copy the language-respective utility to the solution's path*

## Table of Contents
- [Remove Duplicate Words](./duplicate-words/PROBLEM.md)
- [String Replacement Dictionary](./dictionary-replacer/PROBLEM.md)
- [Roman Numeral Converter](./roman-numerals/PROBLEM.md)
