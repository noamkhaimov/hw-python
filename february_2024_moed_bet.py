"""
Question 1
Task: Write a function that accepts a list of numbers and a command string, then returns:

"max": The maximum value.
"min": The minimum value.
"sum": The sum of the numbers.
"jump": A list of numbers at even indices.
An error message and 0 for invalid commands.
"""

def numbers_command(numbers, command):
    if command == "max":
        return max(numbers)
    elif command == "min":
        return min(numbers)
    elif command == "sum":
        return sum(numbers)
    elif command == "jump":
        return numbers[::2]
    else:
        return "Invalid command", 0
print(numbers_command([1, 2, 3, 4, 5, 6], "jump"))  # [1, 3, 5]

"""
Question 2
Part 1: Vehicle Class (20 Points)
Task:

Implement a Vehicle class with:
Protected attributes: color and number_of_wheels.
A static attribute to ensure unique vehicle_id.
Overridden equality (__eq__) and hash (__hash__) methods.

Part 2: Car Class (10 Points)
Task:
Inherit from Vehicle and add:
Protected attributes: model and company.
Override __str__ to format as:
The car <vehicle_id> is of model <company> <model>
"""
class Vehicle:
    _next_id = 0  # Static attribute to ensure unique vehicle_id
    def __init__(self, color: str, number_of_wheels: int):
        self._color = color
        self._number_of_wheels = number_of_wheels
        self._vehicle_id = Vehicle._next_id
        Vehicle._next_id += 1

    @property
    def color(self): # Getter method
        return self._color
    @property
    def number_of_wheels(self): # Getter method
        return self._number_of_wheels
    @property
    def vehicle_id(self): # Getter method
        return self._vehicle_id

    def __eq__(self, other): # Equality method
        if isinstance(other, Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False
    def __hash__(self): # Hash method
        return hash(self.vehicle_id)
v1 = Vehicle("Red", 4)
v2 = Vehicle("Blue", 2)
vehicle_dict = {
    v1: "Car",
    v2: "Bike"
}
class Car(Vehicle):
    def __init__(self, color: str, number_of_wheels: int, model: str, company: str):
        super().__init__(color, number_of_wheels)
        self._model = model
        self._company = company

    def __str__(self):
        return f"The car {self.vehicle_id} is of model {self._company} {self._model}"
    def __hash__(self):
        return hash(self.vehicle_id)
c1 = Car("Red", 4, "Civic", "Honda")
c2 = Car("Blue", 4, "City", "Honda")
c3 = Car("Black", 2, "Activa", "Honda")
print(c1)  # The car 2 is of model Honda Civic
print(c2)  # The car 3 is of model Honda City
print(c3)  # The car 4 is of model Honda Activa
print(vehicle_dict[v1])  # Car

"""
Question 3 (32 Points)
Part 1: Random Array Summation (16 Points)
Task:

Create a 5×5 array of random integers between 20 and 40.
Compute and print the sum.
"""
import numpy as np
arr = np.random.randint(20, 41, (5, 5)) # Create a 5×5 array of random integers between 20 and 40
print(arr) # Print array
print(arr.sum()) # Compute and print the sum

"""
Part 2: DataFrame Manipulation (16 Points)
Task:

Read tickets.csv into a DataFrame.
Add a new column "total_price" as the product of "num_of_tickets" and "price".
Save to new_tickets.csv.
"""
import pandas as pd
df = pd.read_csv("tickets.csv") # Read tickets.csv into a DataFrame
df["total_price"] = df["num_of_tickets"] * df["price"] # Add a new column "total_price" as the product of "num_of_tickets" and "price"
df.to_csv("new_tickets.csv", index=False) # Save to new_tickets.csv

print("File saved successfully") # Print message
print(df.head()) # Print first 5 rows of DataFrame

"""
Part 3: Scatter Plot (16 Points)
Task:

Create a scatter plot with: 
x=arr, y=1/arr. 
x-axis linear, y-axis logarithmic.
"""
import numpy as np
import matplotlib.pyplot as plt
arr = np.arange(1, 101) # Create an array of random integers between 1 and 100
plt.scatter(arr, 1/arr) # Create a scatter plot with x=arr, y=1/arr
plt.yscale("log") # Set y-axis logarithmic
plt.title("Scatter Plot") # Set title
plt.xlabel("X-axis") # Set x-axis label
plt.ylabel("Y-axis") # Set y-axis label
plt.legend(["1/arr"]) # Set legend
plt.show() # Display plot

"""
Question 4 (28 Points)
Part 1: SpecialNumber Class (7 Points)
Task:
Create a SpecialNumber class that allows:

Adding two SpecialNumber objects.
Adding a SpecialNumber with an int.
my_num_1 = SpecialNumber(1)
my_num_2 = SpecialNumber(2)
my_num_3 = my_num_1 + my_num_2  # SpecialNumber(3)
my_num_4 = my_num_1 + 5         # SpecialNumber(6)
my_num_5 = 5 + my_num_1         # SpecialNumber(6)
"""

class SpecialNumber:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other): # Adding two SpecialNumber objects
        if isinstance(other, SpecialNumber): # Check if other is an instance of SpecialNumber
            return SpecialNumber(self.num + other.num) # Return SpecialNumber object
        elif isinstance(other, int): # Check if other is an integer
            return SpecialNumber(self.num + other) # Return SpecialNumber object
        raise TypeError("Invalid operand type(s)") # Raise TypeError if invalid operand type(s)

    def __radd__(self, other): # Adding a SpecialNumber with an int
        return self.__add__(other) # Call __add__ method

    def __repr__(self): # Representation method
        return f"SpecialNumber({self.num})" # Return representation

my_num_1 = SpecialNumber(1) # Create SpecialNumber object
my_num_2 = SpecialNumber(2) # Create SpecialNumber object
my_num_3 = my_num_1 + my_num_2  # SpecialNumber(3) # Add two SpecialNumber objects
my_num_4 = my_num_1 + 5         # SpecialNumber(6) # Add a SpecialNumber with an int
my_num_5 = 5 + my_num_1         # SpecialNumber(6) # Add a SpecialNumber with an int
print(my_num_3)
print(my_num_4)
print(my_num_5)

"""
Part 2: What is enum? (7 Points)
Task:
Explain enum and its usage.
Provide an example with at least three options.
"""
"""
Definition:

enum is a module that defines enumerations,
a set of symbolic names bound to unique, constant values.
Usage:

Improves code readability.
Useful for defining constants (e.g., days of the week, states)."""
from enum import Enum
class Color(Enum):
    RED = 1 # Red
    GREEN = 2 # Green
    BLUE = 3 # Blue
print(Color.RED) # Color.RED
print(Color.GREEN) # Color.GREEN
print(Color.BLUE) # Color.BLUE

for color in Color:
    print(color) # Red, Green, Blue

"""
Part 3: What is a property? (7 Points)
Task:

Explain the property decorator and why it is useful.
Discuss why it might be misused or cause problems.
"""
"""
Definition:

property is a built-in decorator used to define getter, setter,
and deleter methods for class attributes.

Advantages:

Allows controlled access to private attributes.
Improves code readability and maintainability.

Potential Problems:

Overuse of property can make code harder to debug.
Avoid heavy computations in getter methods as it can slow down the code.
"""
class Circle:
    def __init__(self, radius): # Constructor method
        self._radius = radius

    @property # Getter method
    def radius(self):
        return self._radius # Return radius

    @radius.setter # Setter method
    def radius(self, value):
        if value < 0: # Check if value is negative
            raise ValueError("Radius cannot be negative") # Raise ValueError
        self._radius = value # Set radius

circle1 = Circle(5)
print(circle1.radius) # 5
circle1.radius = 10
print(circle1.radius) # 10
circle1.radius = -1 # ValueError: Radius cannot be negative
print(circle1.radius) # 10

"""
Part 4: Jupyter Notebook vs PyCharm (7 Points)
Task:
Compare the use of Jupyter Notebook and PyCharm, including their pros and cons.
"""
"""
Feature             	Jupyter Notebook	                            PyCharm
Best For	     Data exploration, visualization, prototyping	Full-fledged application development
Ease of Use	          Interactive and simple                          	Requires project setup
Visualization	   Excellent for data visualization            	Limited inline visualization
Code Organization	  Limited, cell-based                            	Project-based
Performance 	   Slower for large-scale code                 	Optimized for large-scale projects

When to Use:

Jupyter Notebook: For data science, exploratory analysis, and visualization.
PyCharm: For software development, debugging, and version control.
"""

"""
Part 5: What is CSV? (7 Points)
Task:

Explain what CSV is and why it is used.
Provide an example of working with CSV files in Python.
"""
"""
Solution:
Definition:

CSV (Comma-Separated Values) is a plain text format for storing tabular data.
Each row represents a record, and columns are separated by commas.

Usage:

Widely used for data transfer between systems.

"""
import csv

# Writing to a CSV file
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]] # Data to write
with open("people.csv", "w", newline="") as file: # Open file in write mode
    writer = csv.writer(file) # Create CSV writer
    writer.writerows(data) # Write data to file

# Reading from a CSV file
with open("people.csv", "r") as file: # Open file in read mode
    reader = csv.reader(file) # Create CSV reader
    for row in reader: # Iterate over rows
        print(row) # Print row


