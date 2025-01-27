"""
Question 1.
Task:
Write code that receives N numbers from the user and prints their average.

Input Format:

The program requests the number of inputs
𝑁
N.
The program then requests
𝑁
N numbers as input.
Output Format:

Print the average of the numbers.
"""
def find_average():
    print("Enter the number of inputs:")
    N = int(input())
    print("Enter the numbers:")
    sum = 0
    for i in range(N):
        sum += float(input())
    print(sum/N)
find_average()

"""
Question 2.
Task:
Implement two classes according to the given instructions.
Part 1: Class Person (20 Points)
Requirements:

The class should have the following attributes:

person_id, name, and age as protected attributes.
These attributes are passed as parameters to the constructor.
Validation: Ensure no two objects have the same person_id. If a duplicate is detected, raise an appropriate exception.

Use a static dictionary to track existing person_id values.
The class should have the following methods:

sleep: Receives sleep time (in hours) as a parameter and prints:
"The person <name> sleeps for <sleep_time> hours"
work: Receives work time (in hours) and hourly wage, calculates the total wage, and prints:
"The person <name> works for <work_time> hours and earned <wage> shekels"
Override the __str__ method to return:
"The person's name is <name> and they are <age> years old."

Part 2: Class Lecturer (10 Points)
Requirements:

Inherits from the Person class.
Adds the following attributes:
lecture_name and weekly_hours as protected attributes.
These are passed as additional parameters to the constructor.
Overrides the work method:
Calls the parent class's work method, passing weekly_hours as the work_time parameter.
"""

class Person:
    person_id_dict = {}

    def __init__(self, person_id, name, age):
        if person_id in Person.person_id_dict:
            raise Exception(f"Person ID {person_id} already exists")

        self._person_id = person_id
        self._name = name
        self._age = age

        Person.person_id_dict[person_id] = self

    def sleep(self, sleep_time: int):
        print(f"The person {self._name} sleeps for {sleep_time} hours")

    def work(self, work_time: int, hourly_wage: float):
        total_wage = work_time * hourly_wage
        print(f"The person {self._name} works for {work_time} hours and earned {total_wage} shekels")

    def __str__(self):
        return f"The person's name is {self._name} and they are {self._age} years old."

class Lecturer(Person):
    def __init__(self, person_id, name, age, lecture_name, weekly_hours):

        super().__init__(person_id, name, age)

        self._lecture_name = lecture_name
        self._weekly_hours = weekly_hours

    def work(self, hourly_wage):
        super().work(self._weekly_hours, hourly_wage)

try:
    person1 = Person(1, "John", 30)
    person2 = Person(2, "Jane", 25)
    person1.sleep(8)
    person2.work(8, 50)
    print(person1)

    person3 = Person(1, "John", 30)
except Exception as e:
    print(e)

lecturer1 = Lecturer(3, "Dr. Smith", 45, "Math", 20)
lecturer1.work(100)

"""
Question 3.
Answer 2 out of 3 parts of the question. Each part requires writing short Python code snippets.
Follow the specific guidelines in each part.

Task 1: (15 Points)
1.  Use numpy to create a 6x4 array containing random values between 0 and 1.
2.  Print the count of values greater than 0.5.
"""
import numpy as np
arr = np.random.rand(6, 4)
print(np.sum(arr > 0.5))

"""
Task 2: (15 Points)
1.  Use pandas to read a CSV file named exam.csv into a DataFrame.
2.  Perform the following actions:
- Print the first 3 rows of the DataFrame.
- Print the total number of rows in the DataFrame.
- Print the total number of columns in the DataFrame.
- Create a numpy array from a column named "grades".
Assume the column "grades" exists in the CSV file.
"""
import pandas as pd
df = pd.read_csv("exam.csv")
print(df.head(3))

print(len(df))
print(len(df.columns))
print(df["grades"].to_numpy(copy = True))

"""
Task 3: (15 Points)
1. Use numpy to create an array named my_arr1 with 7 integers in ascending order.
2. Create a scatter plot where:
- x-axis is my_arr1
- y-axis is my_arr1 raised to the power of 10
3. Set the y-axis to a logarithmic scale.
4. Add a title and legend to the plot.
"""
"""import matplotlib.pyplot as plt
import numpy as np
my_arr1 = np.arange(1, 8)
plt.scatter(my_arr1, my_arr1 ** 10)
plt.yscale("log")
plt.title("Scatter Plot")
plt.legend(["y = x^10"])
plt.show()"""

"""
Question 4.
Task 1: (6 Points)
Task:
Define a class SpecialNumber such that:

It allows division operations:
my_num / 5
5 / my_num

Example:
my_num = SpecialNumber()
new_num = my_num / 5
new_num = 5 / my_num
"""
class SpecialNumber:
    def __truediv__(self, other):
        return 5 / other
    def __rtruediv__(self, other):
        return 5 / other

my_num = SpecialNumber()

new_num = my_num / 5
print(new_num)

new_num = 5 / my_num
print(new_num)

"""
Task 2: (6 Points)
Explain the difference between __str__ and __repr__. When should each be used?
"""
"""
Answer:

__str__:

Purpose: Provides a human-readable string representation of an object.
Usage: Used when print(obj) or str(obj) is called.
__repr__:

Purpose: Provides an unambiguous representation of an object, often used for debugging.
Usage: Called by repr(obj). Ideally, it should return a string that can recreate the object.
"""
class Example:
    def __str__(self):
        return "This is a human-readable string"
    def __repr__(self):
        return "Example()"
obj = Example()
print(str(obj))
print(repr(obj))

"""
Task 3: (6 Points)
Explain what a virtual environment in Python is and why it is useful.
"""
"""
Answer:
What is a Virtual Environment:
A virtual environment is an isolated Python environment with 
its own dependencies and Python interpreter.

Why Use It:
To prevent dependency conflicts between projects.
To ensure a project uses specific versions of libraries without affecting other projects.

Example:
Create a virtual environment: python -m venv my_env
Activate it: source my_env/bin/activate (Linux/Mac) or my_env\Scripts\activate (Windows).
Install libraries specific to the environment: pip install numpy.
"""

"""
Task 4: (6 Points)
Explain the difference between iloc and loc in Pandas. When should each be used?
"""
"""
Answer:

iloc:
Access rows and columns by index positions (integer-based).
"""
df.iloc[0, 1]  # Access the first row and second column
"""
loc:
Access rows and columns by labels (label-based).
"""
df.loc[0, "column_name"]  # Access row with label 0 and column "column_name"

"""
Task 5: (6 Points)
Explain the difference between mutable and immutable classes.
Which type of class should be used as a dictionary key?
"""
"""
Answer:
Mutable Classes:
Their state can be changed after creation.
Examples: list, dict, set.

Immutable Classes:
Their state cannot be changed after creation.
Examples: int, float, tuple, str.
Dictionary Keys:

Only immutable types can be used as dictionary keys because their hash value must remain constant.
"""
# Valid key (immutable)
d = {1: "one"}

# Invalid key (mutable)
key = [1, 2, 3]
# Raises TypeError
# d = {key: "value"}

"""
Task 6: (6 Points)
What are three foundational concepts in sklearn? Briefly explain each.
"""

"""
Answer:
Estimator:
Represents a model or algorithm (e.g., LinearRegression).
Implements the fit() method for training.

Transformer:
Processes data (e.g., scaling, encoding).
Implements fit() and transform() methods.

Pipeline:
Combines multiple processing steps (e.g., transformers and estimators).
Ensures streamlined workflows.
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

