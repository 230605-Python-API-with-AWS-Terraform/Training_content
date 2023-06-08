# Python classes and objects

In Python, a class is a blueprint or a template for creating objects. It defines the attributes (variables) and behaviors (methods) that an object of that class will have. 

```python

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)

# Accessing attributes
print(car1.make)         # Output: Toyota
print(car2.year)         # Output: 2021

# Invoking methods
car1.drive()             # Output: The Toyota Camry is driving.
car2.stop()              # Output: The Honda Accord has stopped.

```
In the code above, we have a class named `Car`. 

- The class Car: line defines the class named Car.
- The `__init__` method is a special method called a constructor. It is executed automatically when an object is created from the class. It initializes the object's attributes (make, model, year) using the values passed during object creation.
- The drive and stop methods are regular methods defined within the class. They define the behaviors or actions that a car object can perform. These methods can access and utilize the object's attributes using the self keyword.
- We then create two objects of the Car class, car1 and car2, by calling the class as if it were a function. 
- The arguments passed to the class are used by the `__init__` method to initialize the objects' attributes.
- We can access the attributes of an object using the dot notation `(object.attribute)`. For example, car1.make retrieves the value of the make attribute of car1.
- We can invoke the methods of an object using the dot notation as well. For example, `car2.drive()` calls the drive method on car2.
- The methods can access the object's attributes using the self parameter, which represents the instance of the object calling the method.

**Instance Variables vs Class Variables**:

Instance variables are unique to each object instance, while class variables are shared among all instances of a class. 

Here's an example:

```python

class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        # Instance variable
        self.radius = radius

    def calculate_area(self):
        # Accessing both instance and class variables
        return Circle.pi * self.radius * self.radius

# Creating instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(7)

# Accessing instance variables
print(circle1.radius)        # Output: 5
print(circle2.radius)        # Output: 7

# Accessing class variable
print(Circle.pi)             # Output: 3.14159

# Calculating area using instance method
print(circle1.calculate_area())    # Output: 78.53975
print(circle2.calculate_area())    # Output: 153.93791

```

In the above code, pi is a class variable that is shared among all instances of the Circle class. Each instance, represented by circle1 and circle2, has its own radius instance variable that is unique to that instance.

**Dunder methods**:

Dunder methods, also known as magic methods or special methods, are special functions in Python that are surrounded by double underscores `(__)`. These methods provide functionality to customize the behavior of classes and objects. Let's explore some common dunder methods with detailed explanations and examples:

`__init__`: 

The `__init__` method is the constructor method that is called when an object is created from a class. It is used to initialize the object's attributes.

```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x, p.y)  # Output: 3 4

```
In this example, the `__init__` method initializes the x and y attributes of the Point class when a new Point object is created.

`__str__`: 

The `__str__` method returns a string representation of the object. It is called by the `str()` function and the print function.

```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)  # Output: (3, 4)

```

In this example, the `__str__` method overrides the default string representation of the Point object. When print(p) is called, it will invoke the `__str__` method and print the customized string representation.

`__len__`: 

The `__len__` method returns the length of an object. It is called by the `len()` function.

```python

class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

s = Stack()
s.items = [1, 2, 3, 4, 5]
print(len(s))  # Output: 5

```

In this example, the `__len__` method is defined for the Stack class. It returns the length of the items list when len(s) is called.

`__add__`: 

The `__add__` method defines the behavior of the + operator for objects of a class. It allows objects to be added together.

```Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
print(v3.x, v3.y)  # Output: 3 7

```

[ref_link for Dunder methods](https://rszalski.github.io/magicmethods/)

