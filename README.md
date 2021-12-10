# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/markgbeckett/python-intermediate-inflammation/workflows/CI/badge.svg?branch=develop)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Document history

10/DEC/21 -- Initial version created.

## Acknowledgements

The software has been developed by the [Software Sustainability Institute](https://www.software.ac.uk) as part of the basic training material for their Intermediate Research Software Engineering course. 

## Licence

Apache License Version 2.0. See the LICENSE.txt file, which should be included in this distribution.

## Joke

Q: Why do computer scientists confuse Halloween and Christmas?

A: Because OCT 31 = DEC 25

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages (using Python 3):

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation and Testing

The software is available on [GitHub](https://github.com/markgbeckett/python-intermediate-inflammation).

Having obtained a copy, you should install it via the commandline using the following (note use of Python 3):

``pip3 install -r requirements.txt``

To test that your installation is working, run the various tests in the test subdirectory. For example:

``python3 tests/test_models.py``

(Note that Windows users may need to specify their Python interpretor using `python` instead of `python3` - please ensure to use a Python 3 interpretor).

Successful tests produce no output.
