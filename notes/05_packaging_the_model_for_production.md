# Packaging the model for production

## 5.6 Intropduction to production code
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
- Tox is a generic virutalenv management and test command line tool
- Agnostic to OS differences