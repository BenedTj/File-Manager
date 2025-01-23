# File-Manager

## 1. Introduction
Python file managemenet script built using Python built-in modules and watchdog module. The script creates directories and places files inside them according to the value of the variables **directory_to_clean** which specifies the path within the user directory for the script to clean, **user_defined** which defines how the resulting directories will be organized by the script (specifics in section 2.) and **make_others_files** which specifies whether or not file types that are not specified within **user_defined** will be organized into a separate *Others* directory.

Additionally, the **user_directory** variable may be changed in order to give more flexibility in terms of the parent path where the script operates.

## 2. **user_defined** convention
TBD

## 3. Dependencies
The only dependency not included within the built-in Python modules that this script relies on is [watchdog](https://python-watchdog.readthedocs.io/en/stable/index.html) 6.0.0. For further information, **requirements.txt** can be consulted
