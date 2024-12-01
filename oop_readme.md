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

**Note**: This guide is a living document. OOP is a vast topic, and there's always more to learn and explore!