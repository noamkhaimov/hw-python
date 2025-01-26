"""
Question 1: (10 Points)
Task:
Write code that:

Receives positive integers from the user, each on a new line.
Prints the three integers in reverse order, each on a new line.
1. The user will enter the first number.
2. If the number is positive, the program will ask for the second number.
3. If the number is not positive or zero, the program will go to print the numbers in reverse order.
! The last number if it is not positive or zero will not be printed.
"""
from pandas import read_csv

numbers = [] # list to store the numbers
while True: # infinite loop
    number = int(input()) # get the number from the user
    if number <= 0: # if the number is not positive
        break # exit the loop
    numbers.append(number) # add the number to the list
for number in reversed(numbers): # iterate over the numbers in reverse order
    print(number) # print the number

"""
Question 2: (30 Points)
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, animal_id, name, age):
        self._animal_id = animal_id
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @abstractmethod
    def make_sound(self, volume, sound_time):
        pass
    def __str__(self):
        return f"The animal name is {self._name} and it {self._age} years old."
class Dog(Animal):
    def __init__(self, animal_id, name, age,):
        super().__init__(animal_id, name, age)
    def make_sound(self, volume, sound_time):
        return f"The dog {self._name} barks {volume} times for {sound_time} seconds." # return the sound of the dog

"""
Question 3: (32 Points)
part 1: (16 Points)
"""
import numpy as np
arr = np.arange(1, 51).reshape(10, 5) # create a 10x5 array with numbers from 1 to 50
arr_columns_sum = np.sum(arr, axis=0) # calculate the sum of each column
print(arr_columns_sum) # print the sum of each column

"""
part 2: (16 Points)
sum of correlation between the all columns
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("exam.csv") # read the data from the csv file
df_corr = df.corr() # calculate the correlation between the columns
df_corr_heatmap = sns.heatmap(df_corr, annot=True, cmap = 'coolwarm') # create a heatmap of the correlation
plt.title("Correlation Heatmap") # set the title of the heatmap
plt.show() # show the heatmap

"""
part 3: (16 Points)
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

arr = np.arange(1, 6) # create an array with numbers from 1 to 5

plt.scatter(arr, arr**2, label = "Y = X^2") # create a scatter plot of the array
plt.scatter(arr, np.sqrt(arr), label = "Y = sqrt(X)") # create a scatter plot of the square root of the array

plt.xlabel("X") # set the x-axis label
plt.ylabel("Y") # set the y-axis label
plt.title("Scatter Plot of Y = X^2 and Y = sqrt(X)") # set the title of the plot
plt.legend() # show the legend
plt.show() # show the plot

"""
Question 4: (28 Points)
part 1: (7 Points)
"""
class SpecialNumber:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return SpecialNumber(self.number + other)
    def __radd__(self, other):
        return self.__add__(other)
my_num = SpecialNumber(10) # create an instance of the SpecialNumber class
new_num = my_num + 5 # add 5 to the number
new_num2 = 5 + my_num # add 5 to the number
"""
part 2: (7 Points)
"""
class Shape:
    def __init__(self, name):
        self.name = name
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Square(Shape):
    def __init__(self, name, side):
        super().__init__("Square")
        self.side = side
    def area(self):
        return self.side ** 2
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
t1 = Triangle("Triangle", 10, 5) # create an instance of the Triangle class
s1 = Square("Square", 5) # create an instance of the Square class
c1 = Circle("Circle", 3) # create an instance of the Circle class
print(t1.area()) # print the area of the triangle
print(s1.area()) # print the area of the square
print(c1.area()) # print the area of the circle

"""
part 3: (7 Points)
1. What is static method?
2. How it is different from class method?
3. How we can define a static method in a class?
4. How we will use a static method?
"""

"""
Definition:

A static method is a method in a class that does not require access to the instance (self) or the class (cls).
It is declared using the @staticmethod decorator.

Differences from a regular method:

A regular method requires a self parameter and can access instance attributes.
A static method does not require self or cls and cannot access or modify instance or class-level data.

When to use:
Use static methods for utility functions or when the method logic does not depend on the instance or the class.
"""
class MyClass:
    @staticmethod
    def my_static_method():
        return "This is a static method"
print(MyClass.my_static_method()) # call the static method

"""
part 4: (7 Points)
Explanation:
1. What is the difference between an interpreted language and a compiled language?

Python is called an interpreted language because its code is executed line by line by the Python interpreter,
rather than being compiled into machine code beforehand. This allows for faster development and debugging 
but often results in slower execution compared to compiled languages.

Difference from compiled languages:

Interpreted language: Code is executed line by line (e.g., Python).
Compiled language: Code is translated into machine code by a compiler before execution (e.g., C, C++).
Key differences:

Interpreted languages are platform-independent, as the interpreter abstracts the underlying hardware.
Compiled languages tend to have faster runtime performance.
"""

"""
part 5: (7 Points)
"""
"""
Pipelines in sklearn
What are pipelines?
Pipelines are a way to streamline and automate workflows in machine learning.
They allow you to chain together multiple steps, such as preprocessing and model training, into a single object.

Why use pipelines?

They ensure that all transformations are applied consistently to both the training and testing datasets.
They make code more readable and less error-prone.
They simplify hyperparameter tuning, as parameters can be set for the entire pipeline.

Relation to "If it looks like a duck and quacks like a duck":

This refers to Python's concept of "duck typing," 
where the behavior of an object is determined by its methods and properties, not its type.
Pipelines follow this principle, allowing seamless use of various components (e.g., scalers, transformers, estimators) 
as long as they implement the necessary methods (fit, transform, etc.)."""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Fit the pipeline to data
pipeline.fit(X_train, y_train)

# Make predictions
predictions = pipeline.predict(X_test)












