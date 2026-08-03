# Style Guide

The main to keep in mind is that each Python file should be:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

Below are a list of style guidelines recommended based on past personal competitive programming experience:

## Easy to Understand

### One Algorithm, One Import

The idea of this is that if a user requires a specific algorithm or data structure for a problem, they can locate the file in this repository and copy the entire file to their solution for use without any concern for supporting code. For instance, if an algorithm for Range Sum Queries requires the implementation of a segment tree first, then the code necessary to build a segment tree should also be included with the range sum query code.

For the physical codebook however, a more condensed form can be used as repetition should be minimized there. The current plan is that more basic data structures will be included at the start of the codebook in a supporting section, with later more complex algorithms being able to reference this base code as necessary.

### Comments

Each codefile should contain a multiline comment at the start for attribution purposes and for brief explanation of the file roughly in this format:

```python
"""
Author: Github username
Last updated: Date of commit

NOTE: Include NOTE if the file is WIP or has critical issue for later fix

Explanation of what this algorithm/data structure does, 
include important runtimes

func_a(x,y)
Brief description of func_a

func_b(x,y)
Brief description of func_b

IMPORTANT NOTES:
Other important considerations with the code that may affect competitive programming use
"""
```

Other comments in the code are up to coder's discretion, with [PEP-8](https://peps.python.org/pep-0008/) guidelines as a basis.

### Variable Names

Use actually meaningful variable names. There's no need to make them overly long, just one word or a few characters is enough. Having excess single character variable names makes the code impossible to debug in the case where a wrong answer verdict occurs. On the other hand, if your function contains a single `list` variable, keeping track of it with a name like `dynamicProgrammingMemoryArray` is just a "bit" overkill.

## Easy to Modify

### Python Version Compatibility

Code should be implemented in a way so that as early of a `Python 3` version can be supported as possible without comprimisng runtime speed. The environment for this project is setup to use `Python 3.9` intentionally as nearly all online sites use compilers with at least this version or higher, with the exception of the USACO compiler using 3.6. `Python 2` is not a support requirement as it is no longer supported in the ICPC World Finals.

### Keep Code Reasonably Concise

There will be cases where a user copies the code from a file and has to modify small parts of it to fit for a specific problem. Most online competitions are around 2 hours in length, so each of these files should be reasonably concise. There is no explicit limit on the length a file can be, but with that said, avoid adding files that exceed 200+ lines when possible.

### Type Declarations

Only force type declaration if it is absolutely necessary. For instance, consider the basic function below that uses binary search on a sorted array `ar` to return the index `x` where `ar[x] == val`:

```python
def find_value(ar: list, low: int, high: int, val = -1) -> int:
	if high - low <= 1: #at most two vals left, check endpoints
		if ar[low] == val: return low
		elif ar[high]: return high
		else: return -1
	#3+ vals left
	mid = (low+high)//2 #midpoint
	if ar[mid] == val: return mid
	elif ar[mid] > val: return find_value(ar,low,mid,val)
	else: return find_value(ar,mid,high,val)
```

In the above example, `low` and `high` hold index values for the section of the array being searched. Indices in an array are always integers, thus `low` and `high` should be declared as `int`. `ar` must be an array thus it is declared as `list`, but notice that the type of list is not declared. The most common use for this function in competitive programming will be with`list[int]` but it can also work with `list[float]` and `list[str]`. The `val` we are searching for is not guarenteed to be any given type such as `int`, so it is not type declared and kept as an optional variable because Python does not allow mixing declared and undeclared variable types. Lastly, the return type can be declared as `int` since the function is expected to return an integer index value, or -1 if the value was not found in the array.

#### Important note about list declaration
If you are declaring a variable as a `list`, even if you know it will always be a `list[int]` or `list[list]` or `list[x]` just declare it as a `list` only. `list[list]` apparently has consistency issues and results in runtime error on the PyPy3 compiler.

## Practical For Use

### How Complex Should a Concept be for Implementation

While there are legacy files for a [stack](../src/data_structures/Stack.py) and [queue](../src/data_structures/Queue.py) in this repositiory, no further absolute basic data structures will be accepted. In practice these files are unlikely to be used for competitive programming purposes either due to minimal speed improvement at best or very simple existing methods for "implementing" these structures. In this case, a stack can just be implemented as a `list()` with `.pop()` and `.append()` used for removing and adding elements, while a queue can be done with a `list()` and an index pointer. For that matter, priority queue is most simply set up using the existing `heapq` library, so each new file added to this repository should aim to add a new tool of sorts not covered by Python's existing base libraries.

On the other hand, extremely niche algorithms should be avoided for implementation. The priority of additions to this repository is roughly based on the importance each concept has in competitive programming, the usefulness a preset implementation would have, and the reliability of maintaining and testing the implementation. In otherwords, while [Matroid Intersection](https://usaco.guide/adv/matroid-isect?lang=py) may be a useful algorithm to have, the probability that it would be required for a problem, let alone one that most people would actively try to solve is very low. 
