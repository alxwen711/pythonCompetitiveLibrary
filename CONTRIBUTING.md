

This is a relatively new project I've began so all contributions are greatly appreciated. Before contributing please read the [Style Guide](./docs/styleguide.md) for recommended code guidelines. Asides from these there isn't any other requirements other than making the code easy to use and understand.

For creating a new algorithm or data structure file a template exists in [algorithmTemplate.py](./utility/algorithmTemplate.py). For the multiline comment replace all square brackets with the appropriate information; everything else there is optional. Testfiles for quality assurance are also appreciated and a template for creating them is found in [algorithmTemplateTests.py](./utility/algorithmTemplateTests.py).

Once you have made additions in the form of code or documentation, submit a pull request and I will typically review it around 2-4 UTC daily. This is because I do not want to be merging while a CodeForces/CodeChef contest is occurring, and they do not occur at this time. 

If I have not responded to a PR after two weeks without reason then and ONLY then you can follow [this guide](https://stackoverflow.com/questions/12686545/how-to-leave-a-message-for-a-github-com-user) to privately message me. For obvious reasons, please do not abuse the above.


## Style Guide

The main to keep in mind is that each Python file should be:

- Easy to understand
- Easy to modify for specific problems
- Practical for use in competition

Below are a list of style guidelines I recommend based on past competitive programming experience:

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



