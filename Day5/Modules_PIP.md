# Python modules

## Python Module

A module in Python is a file containing Python code that defines functions, classes, and variables. It serves as a reusable unit of code that can be imported and used in other Python programs or scripts. Modules help organize and modularize code, promoting code reusability and maintainability.

**Creating and Importing Modules**:

*Creating a Module*:

To create a module, you simply need to create a Python file with a `.py` extension.
For example, create a file named my_module.py and define some functions or classes in it:

```python

def greet(name):
    print("Hello, " + name)

def add(a, b):
    return a + b
```

This creates a module named my_module with two functions: greet and add.

*Importing a Module*:

To use a module in another Python script, you need to import it using the import statement.
In your main script, import the module my_module and access its functions using dot notation:
```python
import my_module

my_module.greet("Alice")
result = my_module.add(3, 5)
print(result)
```

The output will be:

Hello, Alice
8

The import statement imports the entire module, and you can access its contents using the module name followed by the function or variable name.

*Importing Specific Items from a Module*:


You can also import specific functions or variables from a module, rather than importing the entire module.

For example, to import only the greet function from the my_module module:

```python

from my_module import greet

greet("Bob")
```

This allows you to directly use the imported function without needing to reference the module name.

*Renaming Imported Modules or Items*:

You can use the `as` keyword to rename a module or an imported item to make it more readable or avoid naming conflicts.

For example, to import the my_module module and rename it as mm:
```python

import my_module as mm

mm.greet("Charlie")
```

Similarly, you can rename specific imported items:
```python

from my_module import greet as say_hello

say_hello("David")
```

## Builtin Modules

Python built-in modules are a set of modules that come pre-installed with the Python programming language. These modules provide a wide range of functionalities that are readily available without the need for any additional installations. 

`math`: Provides mathematical functions and constants.

```python

import math

# Compute the square root
root = math.sqrt(16)

# Compute the sine of an angle
sine = math.sin(math.pi / 2)

# Access mathematical constants
pi = math.pi
```

`random`: Offers functions for generating random numbers and making random choices.

```python

import random

# Generate a random integer
num = random.randint(1, 10)

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

# Choose a random element from a sequence
item = random.choice(["apple", "banana", "orange"])

```

`datetime`: Provides classes for manipulating dates, times, and timestamps.

```python
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a specific date
date = datetime.datetime(2022, 5, 15)

# Perform date and time calculations
diff = date2 - date1
```

`os`: Enables interaction with the operating system, allowing file and directory operations.

```python
import os

# Get the current working directory
current_dir = os.getcwd()

# List files in a directory
files = os.listdir(current_dir)

# Rename a file
os.rename("old_name.txt", "new_name.txt")
```

`sys`: Provides access to system-specific parameters and functions.

```python
import sys

# Get command-line arguments
args = sys.argv

# Terminate the program with an exit code
sys.exit(0)
```

`time`: Provides functions for working with time, such as measuring execution time and formatting time values.

```python

import time

# Get the current time in seconds
current_time = time.time()

# Pause the execution of the program for a specified number of seconds
time.sleep(2)

# Format a timestamp into a readable string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```

`json`: Allows for serialization and deserialization of JSON (JavaScript Object Notation) data.

```python

import json

# Serialize Python object to JSON
data = {"name": "John", "age": 30}
json_data = json.dumps(data)

# Deserialize JSON to Python object
python_obj = json.loads(json_data)
```

`csv`: Provides functionality for reading and writing CSV (Comma-Separated Values) files.

```python

import csv

# Read data from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write data to a CSV file
with open('output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])
```

`re`: Offers support for working with regular expressions.

```python

import re

# Match a pattern in a string
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = 'Contact us at info@example.com'
match = re.search(pattern, text)

if match:
    print('Email found:', match.group())
```

`sys`: Provides access to system-specific parameters and functions.

```python

import sys

# Get command-line arguments
args = sys.argv

# Terminate the program with an exit code
sys.exit(0)
```

---

**PyPI (Python Package Index)**:

PyPI is the official repository for third-party Python packages. It serves as a central hub where developers can publish, share, and discover Python packages for various purposes and domains. PyPI hosts thousands of open-source packages contributed by the Python community.

Key features and functionalities of PyPI include:

`Package Hosting`: PyPI hosts a vast collection of Python packages, covering a wide range of domains such as web development, data analysis, machine learning, scientific computing, and more.

`Package Discovery`: Developers can explore PyPI to discover packages that provide functionalities they need for their projects. They can search for packages by name, keywords, or specific categories.

`Package Metadata`: Each package on PyPI is accompanied by metadata that provides information about the package. Metadata includes details such as the package name, version, description, author, license, dependencies, and project homepage.

`Versioning and Release Management`: PyPI allows package authors to manage different versions of their packages. They can release new versions with bug fixes, feature enhancements, or compatibility updates. This enables developers to choose specific versions based on their requirements.

`Package Installation`: PyPI packages can be easily installed in a Python environment using the pip package manager. pip resolves and downloads package dependencies automatically, simplifying the installation process.

**pip Package Manager**:

pip is the default package manager for Python. It is a command-line tool used for installing, upgrading, and managing Python packages from PyPI. pip interacts with PyPI to download packages and their dependencies and installs them in the desired Python environment.

*Installing a Package*:
To install a package from PyPI, you can use the pip install command followed by the package name. For instance, to install the popular package requests for making HTTP requests, run the following command:

```python

pip install requests

```
This command will download the requests package and its dependencies from PyPI and install them in your Python environment.

*Upgrading a Package*:

You can upgrade a package to its latest version using the pip install --upgrade command. For example, to upgrade the requests package, run the following command:

```

pip install --upgrade requests

```

*Listing Installed Packages*:

You can list all the packages installed in your Python environment using the pip list command. It will display the package names along with their versions. Run the following command:

```
pip list

```

*Uninstalling a Package*:

If you want to remove a package from your Python environment, you can use the pip uninstall command followed by the package name. For example, to uninstall the requests package, run the following command:

```
pip uninstall requests
```

---

## venv

venv is a built-in Python module that allows you to create virtual environments. A virtual environment is an isolated Python environment that has its own set of installed packages and dependencies, separate from the global Python environment. This isolation helps prevent conflicts between different projects that may have different package requirements.


*Creating a Virtual Environment*:

Start by opening your command prompt or terminal and navigate to the desired directory where you want to create the virtual environment. Then, run the following command to create a virtual environment named "myenv":
```
python -m venv myenv

```

This command will create a new directory named "myenv" in your current location, which will contain the necessary files for the virtual environment.

*Activating the Virtual Environment:*

After creating the virtual environment, you need to activate it to start using it. The activation process varies depending on your operating system:

On Windows, run the following command:
```
myenv\Scripts\activate
```
On Unix-based systems (Linux, macOS), run the following command:
```bash
source myenv/bin/activate
```

Once activated, you will notice that your command prompt or terminal prompt changes to indicate that you are now working within the virtual environment.

*Installing Packages in the Virtual Environment:*

With the virtual environment activated, you can now install packages using pip. For example, let's install the requests package by running the following command:

```
pip install requests
```

This command will download and install the requests package into the virtual environment.

*Running Python Scripts within the Virtual Environment:*

You can now run Python scripts that rely on the packages installed within the virtual environment. For instance, create a file named "script.py" and add the following code:

```python

import requests

response = requests.get("https://www.example.com")
print(response.status_code)
```

Save the file, and from the command prompt or terminal (with the virtual environment activated), run the script using the Python interpreter:

```
python script.py
```

The script will execute and make use of the requests package that was installed within the virtual environment.

*Deactivating the Virtual Environment*:

When you're done working within the virtual environment, you can deactivate it to return to your global Python environment. Simply run the following command:

```
deactivate
```
After deactivating, your command prompt or terminal prompt will return to its original state.

By using venv and creating virtual environments, you can keep your project's dependencies separate and avoid conflicts with other projects. Each virtual environment will have its own set of installed packages, providing a clean and isolated environment for development and deployment.

Remember to activate the virtual environment every time you want to work on the project and use pip to install, upgrade, or manage packages within that environment.

---


