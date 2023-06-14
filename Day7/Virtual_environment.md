**What is Virtual Environment in Python ?**

Virtual Environment is a kind of a container which runs specific version of Python and its modules. And it is used in the cases where you are working on two different project which has different dependencies. Say one of your project uses Django 1.11 and another one uses Django 2.0. In that case you will be needing Virtual Environment.

**Why do we need to use Virtual Environment in Python?**

There are cases when you are working on different projects and you want to have different versions of Python for different project say Python 3.7 and Python 3.8. Using, virtual environments, you can use different versions of Python as well as the modules installed in it. E.g. in Kivy supports only upto version 3.7 but the latest version of Python is 3.8 so in order to install and run Kivy I have used Virtual Environment to run Python 3.7 in this tutorial video of kivy in which you can learn to build a stopwatch in Python using Kivy.



**Virtualenv vs Venv? How to install Virtualenv?**
Prior to Python 3 i.e. in Python 2.7, you will have to install the module called virtualenv to create virtual environments in Python. It is a third party module and you can still install virtualenv in Python 2.7 as well as Python 3 and above using pip.
```python

pip install virtualenv
```
But Python 3 and above, ships with an inbuilt module called venv, which solves the same purpose as of virtualenv i.e. it helps to create and use virtual environments in Python.

**How to create a Virtual Environment in Python?**

We will be using venv to create virtual environment in Python as I assume that all of you are using Python 3 as the support for the legacy version i.e. Python 2.7 has already ended. However, if you are still using Python 2.7 just replace venv with virtualenv in all the codes to create a virtual environment in Python 2.7.

Now, to create a virtual environment in Python using venv your will have to use the following code :-
```python

python -m venv name-of-the-env
```

**How to create a Virtual environment using different versions of Python?**

If you want to create a virtual environment using a specific version of Python then first of all you must have that version installed in your computer and then you will have to check how you run that version of python e.g. in my system I can run Python 3.7 and Python3.8 using python3 and python3.8 respectively in the terminal.

So in order to create a Virtual Environment using Python version 3.7, I will have to use :
```python

python3 -m venv name-of-the-env
```


**How to activate a Virtual Environment in Python?**

To activate the Virtual Environment on a Windows Machine, you will have to use the following command:-
```
. .\name-of-the-env\Scripts\activate

```

**How to deactivate the Virtual Environment in Python?**

To deactivate the Virtual Environment on all the operating systems like MacOS, Linux and Windows, you just have to type deactivate in the terminal/powershell/command line.

deactivate

**Shortcut to create a Virtual Environment in Python**
Instead of naming the venv/virtual environment everytime, you can create a virtual environment with the name of the directory in which you are working by using a period (.) at the end. So, in order to create such virtual environment on all the operating systems, you will have to type the following command :-

```
python3 -m venv .
```
And to activate this on MacOS and Linux
```
source bin/activate
```
On Windows:
```
. .\Scripts\activate
```
