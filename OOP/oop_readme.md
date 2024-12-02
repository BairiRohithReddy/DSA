# Object-Oriented Programming in Python

OOP allows us to create custom data types tailored to our specific needs, instead of relying solely on pre-existing types.

## Core Components of OOP

1. **Object**
2. **Class**
3. **Polymorphism**
4. **Encapsulation**
5. **Inheritance**
6. **Abstraction**

### Class

A class is a blueprint that defines how an object will behave. In Python, everything is an object, and every object is part of a class. An object cannot exist without a class.

A class contains:
- Data (properties)
- Functions (behaviors)

#### Example of a Class Definition

```python
class Car:
    # Class variables (shared among all instances)
    total_cars = 0

    # Constructor method
    def __init__(self, color, model):
        # Instance variables (unique to each object)
        self.color = color
        self.model = model
        Car.total_cars += 1

    # Instance method
    def calculate_avg_speed(self, distance, time):
        """
        Calculate average speed
        
        :param distance: Total distance traveled
        :param time: Total time taken
        :return: Average speed
        """
        return distance / time if time > 0 else 0
```

### Object

An object is an instance of a class. It represents a specific realization of a class with its own unique data.

```python
# Creating objects
wagnor = Car(color='blue', model='sports')
sedan = Car(color='red', model='sedan')
```

### Method vs. Function

- **Method**: A function defined inside a class
- **Function**: A standalone block of code not bound to any class

### Special Methods (__init__ and Magic Methods)

#### __init__() Method
- A constructor that is automatically called when an object is created
- Used for initializing object attributes
- Configures the object's initial state

#### Magic Methods (Dunder Methods)
- Special methods with double underscores before and after the name
- Automatically triggered in specific scenarios
- Customize object behavior

```python
class Example:
    def __init__(self):  # Constructor
        pass
    
    def __str__(self):  # String representation
        return "Custom string representation"
    
    def __len__(self):  # Defines behavior for len() function
        return 0
```

### Self Keyword

- Refers to the current instance of the class
- Must be the first parameter in instance methods
- Allows access to instance attributes and methods

```python
class MyClass:
    def my_method(self):
        # 'self' refers to the instance calling this method
        print("Accessing the current instance")
```

### Instance Variables

Variables that can have different values for different objects of the same class.

```python
class BankAccount:
    def __init__(self, account_number):
        # Instance variables
        self.account_number = account_number
        self.balance = 0
```

### Private and Public Variables

```python
class SecureAccount:
    def __init__(self):
        # Private variables (name mangling)
        self.__pin = None
        self.__balance = 0
    
    # Public method to access private variable
    def get_balance(self):
        return self.__balance
```

### Encapsulation

Encapsulation involves:
- Hiding internal details
- Controlling access through getter and setter methods
- Protecting data integrity

```python
class User:
    def __init__(self):
        self.__age = 0
    
    # Getter method
    def get_age(self):
        return self.__age
    
    # Setter method with validation
    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Invalid age")
```

### Pass by Reference

Objects are passed by reference in Python:

```python
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    print(f"Hello {customer.name} {'sir' if customer.gender == 'male' else 'ma\'am'}")

# Object is mutable
cust = Customer('Rohith', 'male')
greet(cust)
```

### Static Variables and Methods

```python
class Counter:
    # Class (static) variable
    __total_count = 0

    def __init__(self):
        Counter.__total_count += 1

    # Static method to access class variable
    @staticmethod
    def get_total_count():
        return Counter.__total_count
```

### Class Relationships

#### 1. Aggregation (Has-a Relationship)
- One class contains another class as a component

```python
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Aggregation
```

#### 2. Inheritance (Is-a Relationship)

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        print(f"Driving {self.brand} {self.model}")
```

## Advanced Concepts to Explore

1. Multiple Inheritance
2. Abstract Base Classes
3. Dataclasses
4. Type Hints in OOP
5. Decorators
6. Context Managers

## Best Practices

- Use meaningful and descriptive names
- Follow PEP 8 naming conventions
- Keep classes focused and modular
- Use inheritance judiciously
- Prefer composition over inheritance when possible

## Common Pitfalls

- Overusing inheritance
- Creating overly complex class hierarchies
- Not properly encapsulating data
- Ignoring type hints and documentation

---

### Understanding Classes and Objects
Classes seemed like an unnecessary complexity. Now, I see them as powerful blueprints for creating structured, logical code. Think of a class like a cookie cutter, and objects as the actual cookies – each object is a unique instance created from the same template.

```python
class Developer:
    def __init__(self, name, primary_language, years_of_experience):
        # These are instance attributes
        self.name = name
        self.primary_language = primary_language
        self.years_of_experience = years_of_experience
        # Private attribute (by convention)
        self._project_count = 0
    
    def learn_new_technology(self, tech):
        print(f"{self.name} is learning {tech}")
        
    def complete_project(self):
        self._project_count += 1
        print(f"Project completed! Total projects: {self._project_count}")

# Creating objects
me = Developer("Claude", "Python", 5)
me.learn_new_technology("Machine Learning")
me.complete_project()
```

## 🔗 Class Relationships: The Deeper Dive

### 1. Aggregation (Has-A Relationship)
Aggregation is like having a Swiss Army knife. The knife contains tools, but those tools can exist independently.

```python
class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

class Person:
    def __init__(self, name, contact_address):
        self.name = name
        # Aggregation: Person has an Address, but Address can exist separately
        self.address = contact_address

# The Address can exist independently
home_address = Address("123 Code Street", "Pythonville", "Programland")
john = Person("John", home_address)
```

### 2. Inheritance (Is-A Relationship)
Inheritance is like a family tree. Child classes inherit characteristics from parent classes but can also have their own unique traits.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} is breathing")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming")
    
    # Method overriding
    def fly(self):
        print(f"{self.name} cannot fly")

penny = Penguin("Penny")
penny.breathe()  # Inherited from Animal
penny.swim()     # Specific to Penguin
penny.fly()      # Overridden method
```

## 🎭 Polymorphism: The Shape-Shifter of OOP

### Method Overriding
When a child class provides a specific implementation of a method defined in its parent class.

### Operator Overloading
Making operators work with custom classes:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        # Custom addition for vectors
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses our custom __add__ method
print(v3)  # Prints: Vector(4, 6)
```

## 🚨 Common Pitfalls and Important Notes

### 1. Multiple Inheritance Complexity
Python supports multiple inheritance, but it can lead to the "diamond problem":

```python
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

# Method Resolution Order (MRO) becomes crucial
d = D()
d.method()  # Which method gets called?
print(D.__mro__)  # Shows the method resolution order
```

### 2. Composition Over Inheritance
While inheritance is powerful, composition often leads to more flexible code:

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        # Composition: Car has an Engine, not inherits from Engine
        self.engine = Engine()
    
    def start_car(self):
        self.engine.start()
```

## 🤔 Frequently Asked Questions

### Q: When should I use inheritance vs. composition?
**A**: Use inheritance when you have a true "is-a" relationship. Use composition when you want to build complex objects by combining simpler ones.

### Q: What's the difference between `@classmethod`, `@staticmethod`, and instance methods?
**A**: 
- Instance methods: Work with instance-specific data
- Class methods: Work with class-level data, can modify class state
- Static methods: Utility functions related to the class but not dependent on instance or class state

## 💡 Pro Tips
1. Always use `super()` when extending parent class methods
2. Implement `__str__` and `__repr__` for better object representation
3. Use type hints to make your code more readable
4. Be cautious with multiple inheritance

## 🚀 Continuous Learning
OOP is a journey, not a destination. Keep practicing, experiment with different patterns, and don't be afraid to refactor your code.

## 📚 Recommended Resources
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on classes
- Design patterns books
- Open-source Python projects on GitHub

---
