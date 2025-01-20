"""
Question 1
Task 1: (10 Points)
Task:
Write code that:

Reads three integers from the user.
Reads a command ("sum" or "sort").
Performs the following based on the command:
"sum": Print the sum of the three integers.
"sort": Print the three integers sorted in ascending order.
Input Format:

Three integers followed by a command.
Output Format:
Input	Output
1         6
2
3
sum	       1
4           4
6           6
1
sort
"""
def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    command = str(input("Enter command: "))
    if command == "sum":
        print(x + y + z)
    elif command == "sort":
        print(*sorted([x, y, z]))


"""
Question 2
Task 1: (20 Points)
Implement two classes according to the given instructions.

Requirements:

The class should be abstract.
Include the following abstract methods:
get_perimeter: Calculates and returns the perimeter of the shape.
get_area: Calculates and returns the area of the shape.
Include a static method:
how_many_shapes: Returns the total number of Shape objects created so far.
Use a static attribute to count the shapes.

Part 2: Class Square (10 Points)
Requirements:

Inherits from the Shape class.
Includes the following attributes:
side, x, y as private attributes.
These attributes are initialized in the constructor.
Implements the methods:
get_perimeter: Returns the perimeter as side * 4.
get_area: Returns the area as side^2.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    total_shapes = 0
    def __init__(self):
        Shape.total_shapes += 1
    @abstractmethod
    def get_perimeter(self):
        pass
    @abstractmethod
    def get_area(self):
        pass
    @staticmethod
    def how_many_shapes():
        return Shape.total_shapes

class Square(Shape):
    def __init__(self, side, x, y):
        super().__init__()
        self.__side = side
        self.__x = x
        self.__y = y
    def get_perimeter(self):
        return self.__side * 4
    def get_area(self):
        return self.__side ** 2

square1 = Square(5, 0, 0)
square2 = Square(3, 0, 0)
square3 = Square(7, 0, 0)
print(Shape.how_many_shapes())

"""
Question 3: (32 Points)
Task:
Answer 2 out of 3 parts. Each part involves writing Python code following specific instructions.

Part 1: (16 Points)
Task:

Use numpy to create an array containing numbers from 1 to 5.
Create a 5x5 matrix where each row is the array multiplied by a different scalar.
Print the matrix.
"""
"""import numpy as np
arr = np.arange(1, 6)
matrix = np.arange(1, 6).reshape(-1, 1) * arr
print(matrix)"""

"""
Task 2: (16 Points)
Load a CSV file named exam.csv into a pandas DataFrame.
Perform the following:
- Print the first 7 rows of the DataFrame.
- Print the names of all the columns in the DataFrame.
- Print the value in the column named "name" and row number 148.
"""
"""import pandas as pd
df = pd.read_csv("exam.csv")
print(df.head(7))
print(df.columns)
print(df.loc[148, 'name'])"""

"""
Task 3: (16 Points)
Use numpy to create an array my_arr containing 2000 integers between 1 and 30, with repetitions.
Plot a histogram to display the frequency of each number.
Add a title and legend to the graph.
"""
import matplotlib.pyplot as plt
import numpy as np
my_arr = np.random.randint(1, 31,2000)
plt.hist(my_arr, bins=30, alpha=0.5, label='Frequency of each number')
plt.title("Histogram of Frequency of Each Number")
plt.legend()
plt.show()

"""
Question 4: (28 Points)
Task 1: (7 Points)
Create a ComplexNumber class such that:
It supports function-like calls with an integer parameter.
my_num = ComplexNumber()
some_variable = my_num(5)
"""
class ComplexNumber:
    def __init__ (self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __call__(self, num):
        return num

my_num = ComplexNumber()
some_variable = my_num(5)
print(some_variable)

"""
Task 2: (7 Points)
Explain the difference between a dataclass and a regular class.
Explain why you might prefer to use a dataclass.
Answer:
Differences:
-   A dataclass is a Python decorator (@dataclass) that simplifies 
the creation of classes used primarily to store data.
-   In a regular class, you must manually implement methods like __init__, __repr__, and __eq__.
-   A dataclass automatically generates these methods based on class attributes.
Advantages of dataclass:
-   Reduces boilerplate code.
-   Provides built-in support for immutability (frozen=True).
-   Improves readability and maintainability.
"""
from dataclasses import dataclass
class RegularClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
@dataclass
class DataClass:
    name: str
    age: int

"""
Task 3: (7 Points)
Compare the use cases for Jupyter Notebook and PyCharm, including their pros and cons.
Answer:
When to Use Each:
Jupyter Notebook: When working with data science, creating visualizations, or writing exploratory code.
PyCharm: For complex software development, debugging, and version control.
Feature:                  Jupyter Notebook:                                  PyCharm:
Best for	        Data exploration, visualization, and prototyping	Software development and debugging
Ease of Use	        Simple, interactive interface                   	Requires project setup
Visualization	    Excellent for plots (e.g., Matplotlib, Seaborn) 	Limited inline visualization
Code Organization	Limited, cell-based structure	                    Full project-based structure
Performance	Slower, not ideal for large codebases	                    Optimized for large-scale projects
"""

"""
Task 4: (7 Points)
Explain whether Python variable types are immutable or not,
and compare this behavior to other languages like Java.

Answer:
Are Python Types Immutable?
Immutable types: int, float, str, tuple.
-   Their value cannot be modified after creation.

Mutable types: list, dict, set.
-   Their value can be modified after creation.

Comparison with Java:
In Python, variables are references to objects. Mutability depends on the object type.
In Java, primitive types (int, float) are immutable, but collections (e.g., ArrayList) are mutable.
Example:
# Immutable example
x = 10
x += 1  # Creates a new integer object

# Mutable example
lst = [1, 2, 3]
lst.append(4)  # Modifies the same list object
"""

"""
Task 5: (7 Points)
Explain the difference between a Transformer and an Estimator in sklearn.
Answer:
Transformer:
Used to process data.
Implements fit() and transform() methods.
Example: StandardScaler (scales data).

Estimator:
Represents a predictive model or algorithm.
Implements fit() (to train the model).
Example: LinearRegression, KNeighborsClassifier.

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Transformer
scaler = StandardScaler()
scaled_data = scaler.fit_transform([[1, 2], [3, 4]])

# Estimator
model = LinearRegression()
model.fit(scaled_data, [5, 6])
"""







