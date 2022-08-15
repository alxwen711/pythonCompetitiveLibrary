
## Style Guide

The main to keep in mind is that each Python file should be:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

Below are a list of style guidelines I recommend based on past competitive programming experience:

- Only force type declaration in cases where it is absolutely necessary. For instance, consider the basic function below that uses binary search on a sorted array `ar` to return the index `x` where `ar[x] == val`:

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

In the above example, `low` and `high` hold index values for the section of the array being searched. Indices in an array are always integers, thus `low` and `high` can be declared as `int`. `ar` is assumed to be an array thus the `list` declaration is allowed, but notice that the type of list is not declared because the code above could work with `list[int], list[float], list[str]`. Likewise, the `val` we are searching for is not guarenteed to be any given type such as `int`, so it should not be type declared. `val` is kept as an optional variable because Python does not allow mixing declared and undeclared variable types. Lastly, the return type can be declared as `int` since the function is expected to return an integer index value, or -1 if the value was not found in the array.

- Use actually meaningful variable names. There's no need to make them overly long, just one word or a few characters is enough. Having excess single character variable names makes the code impossible to debug in the case where a wrong answer verdict occurs.



