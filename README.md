# File-Manager

## 1. Introduction
Python file managemenet script built using Python built-in modules and watchdog module. The script creates directories and places files inside them according to the value of the variables `directory_to_clean` which specifies the path within the user directory for the script to clean, `user_defined` which defines how the resulting directories will be organized by the script (specifics in section 2.) and `make_others_files` which specifies whether or not file types that are not specified within `user_defined` will be organized into a separate *Others* directory.

Additionally, the 'user_directory' variable may be changed in order to give more flexibility in terms of the parent path where the script operates.

## 2. `user_defined` convention
`user_defined` is written as a Python dictionary which stores keys referring to the file extension to be captured. The value stored within this dictionary is a tuple with a size of 3.
1. The first element is a String that stores the name of the directory name that we want to put all files with the specified file extension in.
2. The second element is a Python dictionary with the keys being the subdirectory name for a certain subset of files whose file names contain the keywords specified in the tuple that is stored within the value associated with the key.
3. The third and final element is a boolean that specifies whether file names not captured by the keywords found within the second element should be stored in another directory labelled as *Others* or be left untouched.

As an example, if we would like to capture all Microsoft Document files within a directory labelled as *Documents* with subdirectories *University* and *High School* and not having an *Others* directory for the Microsoft Document files not captured by the keywords specified for each subdirectory, we would specify the `user_defined` variable as follows:
```python
# Dictionary that controls what files to be made and how
user_defined = {
    ".docx": ( # file extension of the type of file to be captured.
        "Documents", # name of the directory to be made to store all files
        {
            "University": ("nus", "national university of singapore", "national_university_of_singapore", "nusc", "college"),
            # the key specifies the name of the subdirectories to be made
            # the tuple contains all keywords to be searched in the file name to be captured by the specific subdirectory
            "High School": ("mis", "manado independent school", "manado_independent_school", "sma"),
        },
        False # the boolean specifies whether we should create an 'Others' subdirectory.
    ),
}
```

## 3. Dependencies
The only dependency not included within the built-in Python modules that this script relies on is [watchdog](https://python-watchdog.readthedocs.io/en/stable/index.html) 6.0.0. For further information, **requirements.txt** can be consulted
