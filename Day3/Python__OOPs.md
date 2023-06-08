Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects. OOP is widely used in software development because it helps in reducing the complexity of the code and increases reusability. In this post, we will discuss the main concepts of Object-Oriented Programming.

**1. Class**

A class is a blueprint or a template for creating objects. It is a user-defined data type that consists of data members (attributes or properties) and member functions (methods). The data members are the characteristics of the class, whereas the member functions define the behavior of the class.

In simpler terms, a class defines the attributes and behavior of the objects that will be created from it. In this example, we define a Product class with three attributes: name, price, and quantity. The __init__ method is a special method that is called when an object is created, and it initializes these attributes with the values passed as arguments. We also define a display method that prints the product's name, price, and quantity.

In Python, we define a class using the class keyword. Here's an example of a simple Product class with attributes, and methods.

Example : Creating a class and object

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print(f"{self.name}: ${self.price} ({self.quantity} available)")
```

**2. Objects**

An object is an instance of a class. When a class is defined, no memory is allocated, but when an object is created, memory is allocated. An object has a state (values of its attributes), and it can perform operations (methods). An object can interact with other objects to achieve a task.

In Python, to create an object of the Product class, we can call its constructor method like this:
```python
p1 = Product("Shirt", 29.99, 10)
p2 = Product("Pants", 39.99, 5)

p1.display()  # Shirt: $29.99 (10 available)
p2.display()  # Pants: $39.99 (5 available)
```

**3. Data Abstraction**

Data abstraction is the process of hiding the implementation details of a class and only exposing the necessary information to the user. In Python, data abstraction is achieved through private attributes and methods, which are prefixed with double underscores.

Example : Python’s implementation of Data Abstraction

```python

class Customer:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def display(self):
        print(f"Customer: {self.__name} ({self.__email})")
```

In this example, we define a Customer class with two private attributes: __name and __email. These attributes cannot be accessed directly from outside the class. We also define a display method that displays the customer's name and email.

To access the private attributes, we can define getter and setter methods within the class.
```python
class Customer:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
    
    def display(self):
        print(f"Customer: {self.__name} ({self.__email})")
```

In this updated example, we define get_name and set_email methods to access and modify the private attributes. These methods provide a way to control the access to the attributes and validate the input before setting the values.

**4. Inheritance**

Inheritance is a mechanism that allows a class to inherit properties and methods of another class. The class that inherits the properties and methods is called a child or derived class, and the class that is inherited from is called a parent or base class. Inheritance helps in reusing the code and reducing the complexity of the code.

The child class can override the methods of the parent class and add its own properties and methods. There are four types of inheritance in OOP:

*Single Inheritance*: A child class inherits the properties and methods of only one parent class.
*Multiple Inheritance*: A child class inherits the properties and methods of multiple parent classes.
*Hierarchical Inheritance*: Multiple child classes inherit the properties and methods of a single parent class.
*Multi-level Inheritance*: A child class inherits the properties and methods of a parent class, which itself is a child class of another parent class.
In Python, we can achieve inheritance by defining a derived class that inherits the properties and methods of a base class. Here’s an example of inheritance in Python:

Example : Python’s implementation of Inheritance
```python

class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty
    
    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} year(s)")

```
In this example, we define a ElectronicProduct subclass of the Product superclass. The `__init__` method of the subclass calls the `__init__` method of the superclass using the super() function, which initializes the name, price, and quantity attributes. We also define a warranty attribute specific to electronic products, and a display method that calls the superclass's display method and adds the warranty information.

To create an object of the ElectronicProduct class, we can call its constructor method like this:
```python

e1 = ElectronicProduct("Phone", 499.99, 3, 2)
e2 = ElectronicProduct("Laptop", 1299.99, 2, 3)
e1.display()  # Phone: $499.99 (3 available)
              # Warranty: 2 year(s)
e2.display()  # Laptop: $1299.99 (2 available)
              # Warranty: 3 year(s)
```

**5. Encapsulation**

Encapsulation is the concept of wrapping data and methods in a single unit, known as a class, and controlling access to that unit. In Python, encapsulation is achieved through the use of access modifiers, such as public, private, and protected.

Public attributes and methods can be accessed from anywhere in the program. Private attributes and methods are only accessible within the class, and are denoted by a double underscore prefix (__). Protected attributes and methods are accessible within the class and its subclasses, and are denoted by a single underscore prefix (_).

In the examples above, we used private attributes and methods to achieve data abstraction and encapsulation. The double underscore prefix makes the attributes and methods private, and they can only be accessed within the class.

Example : Python’s implementation of Encapsulation
```python

class Customer:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
    
    def display(self):
        print(f"Customer: {self.__name} ({self.__email})")
```

In this Customer class, the __name and __email attributes are private, and can only be accessed through the get_name and set_email methods. This way, the implementation details of the class are hidden from the user, and the access to the attributes is controlled.

**6. Polymorphism**

Polymorphism is the ability of an object to take on many forms. In OOP, polymorphism allows us to use the same method or operator in different ways for different data types. There are two types of polymorphism:

Compile-time Polymorphism: It is also known as method overloading. In this type of polymorphism, the same method name is used for different methods with different parameters. The compiler chooses the appropriate method to call based on the parameters passed during the function call.
Runtime Polymorphism: It is also known as method overriding. In this type of polymorphism, the same method name and parameters are used in the parent and child class. The child class can override the method of the parent class with its own implementation.
In Python, we can achieve polymorphism using method overloading and method overriding. Here’s an example of method overloading in Python:

Example : Python’s implementation of Polymorphism
```python

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def display_items(self):
        for item in self.items:
            item.display()
```
In this example, we define a ShoppingCart class that has an items attribute and two methods: `add _itemto add items to the shopping cart, anddisplay_itemsto display all the items in the cart. Thedisplay_itemsmethod calls thedisplay` method of each item in the cart.

We can use polymorphism to add both Product and ElectronicProduct objects to the shopping cart, and they will be displayed correctly because they both have a display method with the same name.
```python
cart = ShoppingCart()
cart.add_item(p1)
cart.add_item(e1)

cart.display_items()  # Shirt: $29.99 (10 available)
                      # Phone: $499.99 (3 available)
                      # Warranty: 2 year(s)
```