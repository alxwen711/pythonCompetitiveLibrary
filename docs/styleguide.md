The main to keep in mind is that each Python file should be:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

Below are a list of style guidelines I recommend based on past competitive programming experience:

- Only force type declaration in cases where it is absolutely necessary. For instance, if a variable is keeping track of an index in an array, you may declare it as an int type, but if a variable is only required to be a list, then there is no need to specify what type of list it is (list[int],list[float],list[char],etc.).

- Use actually meaningful variable names. There's no need to make them overly long, just one word or a few characters is enough. Having excess single character variable names makes the code impossible to debug in the case where a wrong answer verdict occurs.



