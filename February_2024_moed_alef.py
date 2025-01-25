"""
Question 1: (10 Points)
Task:
Write a program that:

Reads a sequence of integers from 1 to 20.
Computes the sum of all even numbers in the sequence.
"""
def sum_of_even_numbers():
    numbers = range(1, 21)
    evens = [num for num in numbers if num % 2 == 0]
    total = sum(evens)
    print("The sum of all even numbers in the sequence is:", total)
sum_of_even_numbers()

"""
Question 2: (30 Points)
Part A: MathFunction Class (20 Points)
Task:

Implement an abstract class MathFunction.
Include:
A protected attribute name (provided during initialization).
A property to get the name.
An abstract method calculate(x).
Overridden __str__ to print: Function <name>.
Part B: QuadraticFunction Class (10 Points)
Task:

Inherit from MathFunction to create QuadraticFunction.
Include:
Attributes: a, b, c (coefficients of the quadratic equation).
Implement the calculate(x) method to return ax^2+bx+c.
Default name to "Quadratic Function".
"""
from abc import ABC, abstractmethod
class MathFunction(ABC):
    def __init__(self, name: str):
        self._name = name
    @property
    def name(self):
        return self._name
    @abstractmethod
    def _calculate(self, x: float) -> float: # Abstract method. Must be implemented in subclasses.
        pass
    def __str__(self): # Overridden __str__ to print: Function <name>.
        return f"Function {self._name}."
    def __call__(self, x: float) -> float: # Call the calculate method.
        return self._calculate(x)
class QuadraticFunction(MathFunction):
    def __init__(self, a:float, b:float, c:float, name:str):
        super().__init__(name = "Quadratic Function") # Default name to "Quadratic Function".
        self._a = a
        self._b = b
        self._c = c
    def calculate(self, x: float) -> float: # Implement the calculate method to return ax^2+bx+c.
        return self._a * x**2 + self._b * x + self._c

"""
Question 3: (32 Points)
Answer 2 out of 3 parts.

Part 1: Array Sum (16 Points)
Task:

Create a numpy array with numbers from 1 to 100 divisible by 3.
Compute the sum of the array.
"""
import numpy as np
arr = np.arange(3, 101, 3).reshape((3, 11))
print(arr.sum())
"""
Part 2: Histogram of Prices (16 Points)
Task:

Read car_prices.csv into a pandas DataFrame.
Extract the "price" column into a numpy array.
Plot a histogram of the prices.
"""
"""import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("car_prices.csv")
arr = df["price"].to_numpy(copy = True) # Extract the "price" column into a numpy array.
plt.hist(arr)
plt.show()"""

"""
Task: Plot Two Graphs Side by Side
Requirements:
Create a numpy array named arr containing integers from -10 to 10 in ascending order.
Plot two graphs side by side using plt.subplots:
Graph 1: X = arr, Y = arr
Graph 2: X = arr, Y = −arr (negatives of X)
Add appropriate titles, labels, and legends.
"""
import numpy as np
import matplotlib.pyplot as plt
arr = np.arange(-10, 11)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(arr, arr, label="Y = X")
ax1.set_title("Graph 1")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.legend()

ax2.plot(arr, -arr, label="Y = -X")
ax2.set_title("Graph 2")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.legend()

plt.tight_layout()
plt.show()
"""
Question 4: (28 Points)
Part 1: SpecialNumber Equality (7 Points)
Task:
Enable comparison of SpecialNumber objects based on the num attribute.
"""
class SpecialNumber:
    def __init__ (self, num: int):
        self.num = num
    def __eq__(self, other):
        if isinstance(other, SpecialNumber):
            return self.num == other.num
        return False
my_num_1 = SpecialNumber(num=1)
my_num_2 = SpecialNumber(num=1)
my_num_3 = SpecialNumber(num=2)
print(my_num_1 == my_num_2) # Should print True
print(my_num_1 == my_num_3) # Should print False
print(my_num_1 == 4) # Should print False (with no error)

"""
Part 2: Dataclass Example (7 Points)
Task:
Explain and demonstrate a dataclass.
"""
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    city: str
p = Person(name="Alice", age=25, city="New York")
print(p) # Should print Person(name='Alice', age=25, city='New York')
"""
Part 3: Static Attributes (7 Points)
Task:
Explain and demonstrate a static attribute.
"""
class MyClass:
    static_attribute = 0
    def __init__(self):
        MyClass.static_attribute += 1
print(MyClass.static_attribute) # Should print 0
obj1 = MyClass()
obj2 = MyClass()
print(MyClass.static_attribute) # Should print 2

"""
Part 4(7 Points)
Task: Explain when and why we use:  
if __name__ == "__main__":
"""
# When the Python script is run, the __name__ variable is set to "__main__".
# This allows us to differentiate between when the script is run directly or imported as a module.
# We use if __name__ == "__main__": to execute code only when the script is run directly.
# This is useful when we want to run certain code only when the script is executed directly,
# and not when it is imported as a module.
if __name__ == "__main__":
    print("This code will only run if the script is executed directly.")
    print("It will not run if the script is imported.")
"""
Part 5
Task: Explain what the JSON format is, why it is used, and provide a Python example.
"""
# JSON (JavaScript Object Notation) is a lightweight data interchange format
# that is easy for humans to read and write.
# It is commonly used for transmitting data between a server and a web application,
# as it is language-independent.
# JSON is used to represent structured data in key-value pairs, arrays, and nested objects.
# Python provides the json module to work with JSON data.
# Example:
import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
json_string = json.dumps(data) # Convert Python dictionary to JSON string
print(json_string) # Output: {"name": "Alice", "age": 25, "city": "New York"}

parsed_data = json.loads(json_string) # Convert JSON string to Python dictionary
print(parsed_data) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}







