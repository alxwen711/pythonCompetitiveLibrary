# Contributing

This is a relatively new project so all contributions are greatly appreciated. Before contributing please read the [Code of Conduct](CODE_OF_CONDUCT.md) and [Style Guide](styleguide.md) for recommended code guidelines. Asides from these there isn't any other requirements other than making the code easy to use and understand. Some of the ways to contribute include the following:

- [Reporting and Fixing Bugs](#reporting-and-fixing-bugs)
- [Adding New Algorithm Code](#adding-new-algorithm-code)
- [Submitting Feedback](#submit-feedback)

## A Note on AI Generated Code

There is no explicit restriction against AI generated code. It is reasonable that bots and AI tools can assist in useful contributions for tests and additional algorithm implementations it will be accepted here. However, all AI generated code is expected to follow these conditions:

1. Any AI generated code must be acknowledged within the documentation of the files. This includes to what extent parts of the code were generated via AI tools and in any relevant pull requests the model(s) used for generating the code for potential reproducibility and reliability concerns.

2. All AI generated code must be human reviewed before a pull request. This means that code that was submitted exclusively by an autonoumous agent without any human intervention will not be considered. After all, this is a resource meant to be used for humans in competitive programming.

3. AI generated code will be held to at minimum the same standard expected for all other additions to this repository.

## Development Environment

To setup a sufficient development environment, ensure you have conda installed. Then run the following commands from the base folder:

```bash
conda env create -f environment.yml
conda activate python_cf_env
```

If this is not possible, an environment with `Python>=3.9` and `pytest` setup will likely suffice.

## Reporting and Fixing Bugs

There may be cases where certain parts of the codebook have slow implementations or critical flaws. In these cases report these in the [Issues](https://github.com/alxwen711/pythonCompetitiveLibrary/issues) tab with all sufficient details necessary for reproducing the bug. 

## Adding New Algorithm Code

For creating a new algorithm or data structure file a template exists in [algorithmTemplate.py](utility/algorithmTemplate.py). For the multiline comment replace all square brackets with the appropriate information; everything else there is optional. Testfiles for quality assurance are also appreciated and a template for creating them is found in [algorithmTemplate_test.py](utility/algorithmTemplate_test.py).

Once you have made additions in the form of code or documentation, submit a pull request and I will typically review it within a week assuming there isn't a CodeForces/CodeChef contest occurring, at that time. If I have not responded to a PR after two weeks without reason then and ONLY then you can follow [this guide](https://stackoverflow.com/questions/12686545/how-to-leave-a-message-for-a-github-com-user) to privately message me. For obvious reasons, please do not abuse the above.

### Submit Feedback

For other feedback or suggestions not covered by the previous points, [**Discussions**](https://github.com/alxwen711/pythonCompetitiveLibrary/discussions) can be used.