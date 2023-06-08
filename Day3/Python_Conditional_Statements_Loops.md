# Python conditional statements

In Python, conditional statements allow you to make decisions and execute different blocks of code based on certain conditions. There are primarily two types of conditional statements in Python: 
- if statements
- if-else statement.
- if-elif-else statement

*`if statement`*: The if statement is used to execute a block of code if a specified condition is true. 

Here's the basic syntax:

```python

if condition:
    # Code block to execute if the condition is true
```

*Example*

```python

x = 10

if x > 5:
    print("x is greater than 5")

```

In this example, if the value of x is greater than 5, the code block within the if statement will be executed, and the message "x is greater than 5" will be printed.

*`if-else statement`*: The if-else statement allows you to execute different blocks of code depending on whether a condition is true or false. 

Here's the basic syntax:

```python

if condition:
    # Code block to execute if the condition is true
else:
    # Code block to execute if the condition is false
```

*Example*

```python

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

*`if-elif-else statement`*: The if-elif-else statement allows you to check multiple conditions and execute different blocks of code accordingly. 

Here's the basic syntax:
```python

if condition1:
    # Code block to execute if condition1 is true
elif condition2:
    # Code block to execute if condition2 is true
else:
    # Code block to execute if none of the conditions are true
```

*Example*

```python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

In this example, the code checks multiple conditions. If the value of x is greater than 5, the first code block will be executed. If x is equal to 5, the second code block will be executed. Otherwise, if none of the conditions are true, the code block within the else statement will be executed. In this case, the output will be "x is greater than 5".

---

# Loops

In Python, loops are used to repeatedly execute a block of code until a certain condition is met. 
There are two types of loops commonly used in Python: 
- for loops 
- while loops.

*`for loop`*: A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. Here's the basic syntax:

```python

for element in sequence:
    # Code block to execute for each element in the sequence

```

*Example*

```python

languages = ["python", "Java", "CSharp"]

for lang in languages:
    print(lang)
```

In this example, the for loop iterates over each element in the languages list and prints it. The output will be:

*O/P*

<blockquote>

python
Java
CSharp

</blockquote>

*`while loop`*: A while loop is used to repeatedly execute a block of code as long as a certain condition remains true. 

Here's the basic syntax:

```Python

while condition:
    # Code block to execute as long as the condition is true
```

*Example*

```Python
count = 0

while count < 5:
    print(count)
    count += 1
```

In this example, the while loop continues executing the code block as long as the count variable is less than 5. The value of count is printed in each iteration, and the loop terminates when the condition count < 5 becomes false. The output will be:

<blockquote>

0
1
2
3
4

</blockquote>

*`Loop control statements`*: Python provides loop control statements to modify the execution flow within loops. These statements include break, continue, and else clauses.

- The `break` statement is used to terminate the loop prematurely, even if the loop condition is still true.
- The `continue` statement is used to skip the rest of the code block within the loop for the current iteration and move to the next iteration.
- The `else` clause is used to specify a block of code to be executed when the loop has exhausted all its iterations.

```python

languages = ["python", "Java", "CSharp"]

for lang in languages:
    if lang == "python":
        continue
    elif lang == "CSharp":
        break
    print(lang)
else:
    print("Loop completed")

print("Loop ended")

```

In this example, the loop skips the iteration when the language is "python" using the continue statement. When the language becomes "CSharp", the loop is terminated using the break statement. 

The output will be:

```
apple
Loop ended
```

The "Loop completed" message is not printed because the loop is terminated with the break statement.

---




















