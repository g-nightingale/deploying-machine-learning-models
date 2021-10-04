# Packaging the model for production

## 5.6 Introduction to production code
- Production code is designed to be deployed to end users
- New considerations vs research environment:
    - Testability and maintainability
    - Modularise code
    - Separate config from code where possible
    - Standards such as PEP 8
    - Scalability & performance
    - Reproducibility
- Python packages
    - A module is a python file which contains various Python functions and global variables
    - A package is a collection of modules
        - Requires certain standardised files to be published and installed in other python applications
    - Package structure

        ![Image](images/package_structure.png)


## 6.0 Package requirements files
- Version control
    - Semantic versioning
    - Major.Minor.Patch
    - Major changes breaks the API
    - Minor changes do not break the API
    - Patches fix bugs
- Need to define what versions of our dependencies we expect, and how much risk we are willing to accept with version ranges
- pip install -r requirements.txt

## 6.1 Working with Tox
- Use Tox to trigger train pipeline script
- Tox is a generic virutalenv management and test command line tool
    - Don't have to worry about differerent OS
    - Get same behaviour across platforms
    - Don't need to setup Python paths or configure environment variables
- Agnostic to OS differences
- [] Square brackets represent different tox environments
    - Creates a virtual environment in the .tox hidden directory
- [tox] → default env
- [testenv] → like a base class
    - Commands will be replicated whenever we inherit from this base class testenv
    - e.g.: [testenv:test_package]
- Use tox -e <env-name> to specify an environment to run
- Need to be in same directory as tox.ini file, use cd in command prompt

## 6.3 Package config
- Why use YAML for configuration?
    - Want to limit power of config files
    - Remove temptation to add functionality that might add risks and bugs
    - Can be edited by devs who don't know Python
- def func(**kwargs)
    - Function only takes keyword arguments
    - E.g.: func(a=1, b=2)

## 6.5 Introduction to Pytest
- Defacto standard in industry
- Richer assert statements during failures
- Auto discovery of test modules and functions
- Modular fixtures 
- Backwards compatible with unit test library

## 6.6 Feature engineering code in the package
- Feature engineering is a very common source of bugs
- Important to test all feature engineer code
- Need to be thorough in test coverage

## 6.7 Making predictions with the package
- Check multiple rows or a subset of a dataset
- Set tolerances appropriate to risk appetite

## 6.8 Building the package
- A package is a collection of python modules
- Notoriously complex, debate in the Python community around best practice
- Relevant files:
    - pyproject.toml
        - Lines 1-6 specify basic dependencies to install the package
        - Rest of file is used for configuring tooling
    - setup.py
        - This is where the majority of packaging functionality lives
        - Package meta-data, requirements
    - MANIFEST.in
        - Which files should be included and excluded in the package
- Building the package
    - Need to install PyPA's build
        - conda install --channel conda-forge build
        - pip install --upgrade build
    - Build package
        - python -m build
    - dist directory
        - .whl → faster to install
        - .tar → legacy
    - tid_regression_model.egg-info

## 6.9 Tooling
- test_requirements.txt
    - black → code styling enforcement tool, reformats code if it's not PEP8
    - flake8 → linting tool 
    - mypy → type checking tool
    - isort → ensures imports are in the correct order
- These checks are being used on the different directories
- These tools make our code easier for other people to use, and reduce chance of introducing bugs
- mypy.ini
    - COnfigures what sorts of type hints we are going to worry about



