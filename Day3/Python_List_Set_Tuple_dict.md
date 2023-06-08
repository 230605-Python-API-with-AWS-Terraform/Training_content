## List

A list is an ordered collection of items, and it is one of the most commonly used data structures in Python. 
```python
# Creating a list
fruits = ['apple', 'banana', 'orange', 'mango']

# Accessing elements
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'orange'

# Modifying elements
fruits[1] = 'grape'
print(fruits)  # Output: ['apple', 'grape', 'orange', 'mango']

# Appending elements
fruits.append('pineapple')
print(fruits)  # Output: ['apple', 'grape', 'orange', 'mango', 'pineapple']

# Removing elements
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'grape', 'mango', 'pineapple']

# Slicing
sliced_fruits = fruits[1:3]
print(sliced_fruits)  # Output: ['grape', 'mango']

# Length of the list
print(len(fruits))  # Output: 4

# Iterating over elements
for fruit in fruits:
    print(fruit)

```

**Explanation**:

- The fruits list is created with four elements: 'apple', 'banana', 'orange', and 'mango'.
- Elements in a list are indexed starting from 0. fruits[0] retrieves the first element, which is 'apple'.
- Lists are mutable, meaning you can modify individual elements by assigning new values to specific indices. `fruits[1] = 'grape'` changes the second element to 'grape'.
- The `append()` method adds a new element to the end of the list. `fruits.append('pineapple')` appends 'pineapple' to the list.
- The `remove()` method removes the specified element from the list. `fruits.remove('orange')` removes 'orange' from the list.
- Slicing allows you to extract a portion of the list. `fruits[1:3]` creates a new list containing elements at indices 1 and 2: `['grape', 'mango']`.
- The `len()` function returns the number of elements in the list. `len(fruits)` returns 4.
- You can iterate over the elements of a list using a for loop.

**List Comprehensions**:

List comprehensions provide a concise way to create lists based on existing lists or other iterable objects. They allow you to perform operations on each element of the original list and generate a new list.

```python

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

*Explanation*:

- The list comprehension [x**2 for x in numbers] creates a new list where each element is the square of the corresponding element in the numbers list.
- List comprehensions are concise and readable, especially for simple transformations or filtering operations.

**List Methods**:

Lists provide several built-in methods that allow you to perform common operations, such as sorting, counting occurrences, extending, and more.

Example:

```python
fruits = ['apple', 'banana', 'orange', 'mango']

# Sorting the list
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange']

# Counting occurrences
count = fruits.count('apple')
print(count)  # Output: 1

# Extending the list
fruits.extend(['grape', 'pineapple'])
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange', 'grape', 'pineapple']

# Reversing the list
fruits.reverse()
print(fruits)  # Output: ['pineapple', 'grape', 'orange', 'mango', 'banana', 'apple']
```
*Explanation*:

- The `sort()` method sorts the elements of the list in ascending order.
- The `count()` method returns the number of occurrences of a specific element in the list.
- The `extend()` method adds multiple elements to the end of the list.
- The `reverse()` method reverses the order of the elements in the list.

**Nested Lists**:

Lists can contain other lists as elements, allowing you to create nested structures or matrices.

```python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])  # Output: 6
```
*Explanation*:

- The matrix list contains three nested lists, forming a 3x3 matrix.
- To access an element within the nested list, you can use multiple indices. `matrix[1][2]` retrieves the element at row 1, column 2, which is 6.

**List Slicing**:
List slicing allows you to extract a portion of a list by specifying a start index, an end index, and an optional step size. It returns a new list containing the selected elements.

```python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extracting a sub-list
sub_list = numbers[2:7]
print(sub_list)  # Output: [3, 4, 5, 6, 7]

# Slicing with step size
step_list = numbers[1:9:2]
print(step_list)  # Output: [2, 4, 6, 8]

# Reversing a list
reverse_list = numbers[::-1]
print(reverse_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

*Explanation*:

- The slice `numbers[2:7]` extracts elements from index 2 to 6 (excluding index 7) from the numbers list.
- The slice `numbers[1:9:2]` extracts elements from index 1 to 8 (excluding index 9) with a step size of 2, resulting in `[2, 4, 6, 8]`.
- Slicing with a negative step size, such as numbers[::-1], reverses the order of the elements in the list.

**List Concatenation and Repetition**:

Lists can be concatenated using the `+` operator, which combines two or more lists into a single list. Lists can also be repeated using the `*` operator, which creates a new list with multiple copies of the original list.

```python

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
concatenated = list1 + list2
print(concatenated)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3
print(repeated)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

*Explanation*:

- The concatenation operation list1 + list2 combines the elements of list1 and list2 into a single list.
- The repetition operation list1 * 3 creates a new list that repeats the elements of list1 three times.

**List Membership and Iteration**:

You can check if an element is present in a list using the in operator. Lists can also be iterated over using a for loop to access each element sequentially.
```python
fruits = ['apple', 'banana', 'orange']

# Membership test
print('apple' in fruits)  # Output: True
print('grape' in fruits)  # Output: False

# Iteration
for fruit in fruits:
    print(fruit)
```

---

## Tuples

*`len()`*: 

Returns the number of elements in a tuple.

```python

my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)  # Output: 5
```

*`Indexing and Slicing`*: 

Tuples support indexing and slicing operations similar to lists.

```python

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2:4])  # Output: (3, 4)
```

*`count()`*: 

Returns the number of occurrences of a specified value in a tuple.

```python

my_tuple = (1, 2, 3, 3, 4, 5)
count = my_tuple.count(3)
print(count)  # Output: 2
```

*`index()`*: 

Returns the index of the first occurrence of a specified value in a tuple.

```python

my_tuple = (1, 2, 3, 4, 5)
index = my_tuple.index(3)
print(index)  # Output: 2
```

*Tuple Concatenation*: 

Tuples can be concatenated using the `+` operator.
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print(concatenated)  # Output: (1, 2, 3, 4, 5, 6)
```

*Tuple Repetition*: 

Tuples can be repeated using the * operator.
```python

my_tuple = (1, 2)
repeated = my_tuple * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)
```

*Iteration*: 

Tuples can be iterated over using a for loop.

```python

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
```

---

## Set

A set is an unordered collection of unique elements. It is defined by enclosing comma-separated values within curly braces {}. Sets are mutable, which means you can add, remove, or modify elements in a set. 

Here's an explanation of some commonly used methods and operations with sets in Python:

**Creating a Set**:

```python

my_set = {1, 2, 3, 4, 5}  # Creating a set with initial values
empty_set = set()         # Creating an empty set

```

**Adding Elements**:

```python

my_set.add(6)     # Add a single element to the set
my_set.update([7, 8, 9])  # Add multiple elements using iterable (e.g., list)

```

**Removing elements**:

```python

my_set.remove(3)    # Remove a specific element from the set
my_set.discard(4)   # Remove an element (if present), but do nothing if it doesn't exist
my_set.pop()       # Remove and return an arbitrary element from the set
my_set.clear()     # Remove all elements from the set

```

**Checking Membership**:

```python

2 in my_set    # Check if an element is present in the set (returns True)
6 not in my_set  # Check if an element is not present in the set (returns False)

```

**Set operations**:

```python

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.union(set2)        # Returns a new set with all unique elements from both sets
set1.intersection(set2)  # Returns a new set with common elements between both sets
set1.difference(set2)    # Returns a new set with elements in set1 but not in set2
set1.symmetric_difference(set2)  # Returns a new set with elements in either set, but not both

```

**Set size and iteration**

```python
len(my_set)       # Get the number of elements in a set
for item in my_set:
    print(item)   # Iterate over the elements of the set (order is not guaranteed)
```

---

## Python Dictionary

In Python, a dictionary is an unordered collection of key-value pairs. It is defined by enclosing comma-separated key-value pairs within curly braces {}. Each key-value pair in a dictionary is separated by a colon :. 

Dictionaries are also known as associative arrays or hash maps. Here's an explanation of some commonly used methods and operations with dictionaries in Python:

**Creating a Dictionary**:

```python

my_dict = {"name": "John", "age": 30, "city": "New York"}  # Creating a dictionary with initial key-value pairs
empty_dict = {}                                           # Creating an empty dictionary
```

**Accessing Values**:

```python
name = my_dict["name"]    # Access the value associated with the "name" key
age = my_dict.get("age")  # Access the value associated with the "age" key using the get() method
```

**Modifying Values**:

```python
my_dict["city"] = "London"  # Update the value associated with the "city" key
my_dict.update({"age": 31, "gender": "Male"})  # Update multiple key-value pairs using the update() method
```

**Adding and Removing Key-Value Pairs**:

```python

my_dict["occupation"] = "Engineer"  # Add a new key-value pair to the dictionary
del my_dict["age"]                  # Remove a specific key-value pair from the dictionary
my_dict.pop("gender")               # Remove and return the value associated with a key
my_dict.clear()                     # Remove all key-value pairs from the dictionary
```

**Checking Membership**:

```python
"name" in my_dict       # Check if a key is present in the dictionary (returns True)
"country" not in my_dict  # Check if a key is not present in the dictionary (returns True)
```

**Dictionary Size and Iteration**:

```python
len(my_dict)        # Get the number of key-value pairs in the dictionary
for key in my_dict:
    print(key, my_dict[key])  # Iterate over the keys and values of the dictionary
```

Dictionaries are commonly used when you want to store and retrieve data based on a unique key. They are useful for tasks such as mapping, counting, and organizing data efficiently.

---

