# Python Competitive Library

TLDR: The eventual goal for this resource is to serve as a Python equivalent for [KACTL](https://github.com/kth-competitive-programming/kactl), the primary codebook for competitive programming in C++. An extensive codebook or similar resource for competitive programmiming in Python does not currently exist online, which this repo aims to resolve.

Go to [Usage](#usage) for basic use cases of this resource.

Go to [Codebook Design](#codebook-design) for coding style and project design decisions, as well as other Python related competitive programming implementation quirks to consider.

Go to [Contributing](#contributing) for directions on how to add to this codebook and for planned future additions.


# Usage

[`src`](src) contains the main code files for various data structures and algorithms that can be copy and pasted efficiently for competitive programming purposes. These files are separated currently into 3 categories:

- [**Algorithms**](src/algorithms) for implementation of DFS/BFS, binary/ternary search, dynamic programming, computational math problems, and other problem solving procedures.

- [**Data Structures**](src/data_structures/) for implementation of trees, graphs, hashmaps, stacks, queues, heaps, and other more complex structures.

- [**Math**](src/math/) for implementation of various math related algorithms (prime numbers, CRT, combinatorics).

The [`tests`](tests) folder contains unit tests for the `src` folder files and focuses on algorithm accuracy. For simpler files there are also basic stress tests to ensure the code created is viable for most competitive programming purposes.

The [`contributing`](contributing) folder contains various markdown files for guidelines on adding/improving this repositiory, see [Contributing](#contributing) for more information.

The [`utility`](utility) folder contains code not fitting into any of the above designations. This can include input shorthands inserted at the beginning of any file for efficiency purpose, testcase generators, or templates for creating new algorithm/data structure files. One example are shorthand functions to make processing input easier found in [baseTemplate.py](src/templates/baseTemplate.py).

## Python Support

This resource is setup to support version Python 3.9 and later, which supports nearly all competitive programming use cases for Python. Additionally from the general [coding style](contributing/styleguide.md) guidelines for this project, you should find most code will have no issues on any Python 3 compiler ([the USACO compiler](https://usaco.org/index.php?page=instructions) uses Python 3.6.9 with NO PyPy speedup which makes USACO Gold and Platinum borderline impossible under Python, but the hope is that this online codebook may be able to bridge this gap.) As Python 2 is no longer supported in the ICPC World Finals, there are currently no plans to implement support for it. 

Generally, there will be minimal if any issues assuming that Python 3 is being used. You can use `conda env create -f environment.yml` and then `conda activate python_cf_env` to setup a basic Python environment that ensures all code runs as intended.

# Codebook Design

## Coding Style

See the [Style Guide](contributing/styleguide.md) for a more detailed explanation. Generally though each file should follow these key guidelines:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

## Testing

Currently, `tests` folder mirrors `src` folder in structure and contains files for testing in a one-to-one relation. Additionally, `utility` folder also contains some test files, and like `tests` folder, all test files having a naming convention ending in `_test.py`. Each respective test file mainly tests for accuracy of the code, with more basic files also having stress tests. Running `pytest .` in the environment setup from [Python Support](#python-support) will run all the tests, with options to run only a folder/subset of tests by replacing the `.` as needed. 

# Contributing

All help to improving the coverage and reliability of this codebook is greatly appreciated. General discussion for the project is setup in [**Discussion Thread**](https://github.com/alxwen711/pythonCompetitiveLibrary/discussions/2) and is mainly for tracking future algorithms/data structures/other files planned for implementation. [Issues](https://github.com/alxwen711/pythonCompetitiveLibrary/issues) can be created in cases where there is a significant logical or efficiency flaw in a current file that can be improved. For more detailed guidelines for contributing, refer to [Contributing Guide](contributing/CONTRIBUTING.md).

## Current Repo Plans

Given the current state of this repository, there is more of a focus on cleaning up the older (pre-2026) files in this repository first. Once this is in an adequate state, I will refer to this thread for directions on what to add next. Asides from this, these are the main additions that are being setup first:

- Egrigious code/algorithm cleanup of old `src` code in [https://github.com/alxwen711/pythonCompetitiveLibrary/issues/4](https://github.com/alxwen711/pythonCompetitiveLibrary/issues/4), 

- [`docs`](docs) folder, which will include the base codebook template similar to [https://github.com/kth-competitive-programming/kactl/blob/main/kactl.pdf](https://github.com/kth-competitive-programming/kactl/blob/main/kactl.pdf) and accompanying files and instructions for generating the codebook. This will initially be very simple with mainly general thought process + basic Python efficiency notes.
