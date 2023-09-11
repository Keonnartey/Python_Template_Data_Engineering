# Python_Template_Data_Engineering
IDS 706: Data Engineering 

## Weekly Mini-project 1-Topic:  

Create a Python GitHub template you use for the rest of class which includes:

## 1. devcontainer

The .devcontainer folder mainly contains two files -

Dockerfile defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
devcontainer.json is a json file that specifies the environment variables including the installed extensions in the virtual environment

## 2. Makefile

The Makefile contains instructions for installing packages (specified in requirements.txt), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term 'Check...' ), and linting the code using pylint


## 3. GitHub Actions
  
Github Actions uses the main.yml file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions
  
## 4. Requirements.txt

The requirements.txt file has a list of packages to be installed for any required project. Currently, my requirements file only contains generic python packages, more specific packages can and will be added depending on scope of projects over time.

This file can also specify the version of the package to be installed - which is something that will be useful when multiple collaborators are working on a project and need the same version of a package installed to avoid issues

## 5. Main and test python scripts

This is an example of [my code](https://github.com/Keonnartey/Python_Template_Data_Engineering/blob/ef368639a4e05db2004fdac43f6251e446e4923b/main.py)
