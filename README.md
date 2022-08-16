# Python Competitive Library
This is a repository containing useful Python files for competitive programming. 

# How to Use
The files are separated into four main folders:

- [**Algorithms**](./algorithms) for implementation of DFS/BFS, binary/ternary search, dynamic programming, computational math problems, and other problem solving procedures.

- [**Data Structures**](./data structures) for implementation of trees, graphs, hashmaps, stacks, queues, heaps, and other more complex structures.

- [**Utility**](./utility) for code that does not fit into one of the other two catagories. This can include input shorthands inserted at the beginning of any file for efficiency purpose or testcase generators. One example are shorthand functions to make processing input easier found in [baseTemplate.py](./templates/baseTemplate.py).

- [**Example Uses**](./exampleuses) for using the above algorithm/data structure templates in actual code for programming contests. Each solution file begins with the programming question it is for as well as the methods from this library used.

# Contributing
This is a relatively new project I've began so all contributions are greatly appreciated. The main to keep in mind is that each Python file should be:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

There is also a WIP [Style Guide](./docs/styleguide.md) that is based around what I feel works best for competitive programming.

For any documentation edits (in Python files or README) simply create a pull request and I'll review it as soon as I can. 

If you want to add a new algorithm or data structure file then use the format given in [algorithm.py](./contributing/algorithm.py) by writing your own code below the intial multiline comment. For the multiline comment replace all square brackets with the appropriate information; everything else there is optional. Testfiles for quality assurance are also appreciated and a template for creating them is found in [algorithmTest.py](./contributing/algorithmTest.py). 

Using newAlgorithm.py is unnecessary if you are contributing to the utility folder.

I will typically review pull requests around 2-4 UTC daily. This is because I do not want to be merging while a CodeForces/CodeChef contest is occuring, and they do not occur at this time. 

If I have not responded to a PR after two weeks without reason then and ONLY then you can follow [this guide](https://stackoverflow.com/questions/12686545/how-to-leave-a-message-for-a-github-com-user) to privately message me. For obvious reasons, please do not abuse the above. 

