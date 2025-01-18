"""
Home Assignment #1 - Advance Python
"""

###################################
# General Guidelines
###################################
"""
In this Homework assignment we will use Python (and OOP in Python) to maintain a small grocery store,
and perform various operations on the store.

Guidelines:
    - After completing each part, you should be able to run the program and test your results (so far).
    - Your program MUST run (if it will not, you will lose most of the points).
    - You can use the code from the lectures and recitations as a base line.
    - Make sure to add documentation - as we saw in class.
    - Keep a clean code.
"""

###################################
# The Assignment
###################################
"""
The assignment contains 5 files:
- home_assigment_1.py - 
    This file - contains guidelines and the task description.
- hw1_main.py - 
    - Contains the main file that you will run.
    - Make sure to run it after you complete each part.
    - Change ONLY the parts you are asked to change or add code to.
- item.py
- milk.py
- pepper.py

"""

###################################
# Part 0 - Personal Details
###################################
"""
In hw1_main.py print the id, name and email of the submitters.
Replace the details in the "Part 0 - Personal Details" section.
"""

###################################
# Part 1 - The Item class
###################################
"""
---
Task 1.0 (nothing to do - only read!)
---
The item class represents a general item.

In the file item.py - create an Abstract Class - and call it Item (already done for you).

In Item class - create 2 methods - get_price and get_name - to return the item's price and name (already done for you).

Note: 
The constructor for the class was already built for you (you will change its body later in this assigment).
Make sure you do not change its signature.

---
Task 1.1
---
Add documentation for the class.

---
TASK 1.2
---
Add 3 ABSTRACT methods to the class:
- put_on_shelf - receives a single int parameter `shelf_id`, returns nothing.
- get_department - receives no parameters, returns a string that represents the item's department.
- print_details - receives no parameters, prints data for the item, returns nothing.

Make sure you add type hints and documentation to all the methods!
"""

###################################
# Part 2 - The Milk
###################################
"""
---
Task 2.0 (nothing to do - only read!)
---
In the file milk.py - create a class - and call it Milk (already done for you).

---
Task 2.1
---
Add documentation for the Milk class.

---
Task 2.2
---
Make Milk inherit from Item.

---
Task 2.3
---
Add a constructor to Milk class:
- Call the super class constructor.
  The name for all milk objects should be "MILK".
  The price is received as a parameter.
- The constructor should receive 2 parameter: 
    * price is float.
    * expiration_date is a string.
- The constructor should declare 1 PROTECTED attributes: expiration_date.
  This attribute is initialized using the received parameter.
- Make sure you add type hints and documentation to the constructor.

---
Task 2.4
---
Implement the put_on_shelf abstract method:
- put_on_shelf - receives a single int parameter `shelf_id`, 
         prints the following message:
            Milk carton is put in the fridge on shelf #<shelf_id>.

         Where:
            * <shelf_id> - should be the received <shelf_id> parameter.

---
Task 2.5
---
Implement the get_department abstract method:
- get_department - receives no parameters and returns the string:
    DAIRY

---
Task 2.6
---
- print_details - receives no parameters, prints data for the milk:
    * The method prints the following text (note the line break):
        Item #<id> - <name> costs <price> nis. It belongs to the <department> department. 
        Should be kept COLD, will expire on <expiration_date>.

    * Where:
        * <id> - should be the item's id (use get_id method)
        * <name> - should be the item's name (use get_name method)
        * <price> - should be the item's price (use get_price method)
        * <department> - should be the item's department name (use get_department method)
        * <expiration_date> - should be the <expiration_date> attribute (received in the constructor)
"""

###################################
# Part 3 - The Pepper
###################################
"""
In this part you will create the pepper class.

In the file - pepper.py - you should create the Pepper class (you can and should change the existing code).

Guidelines:
1. The Pepper class inherits from Item class.
2. The Pepper class receives 3 parameters in its' constructor:
    * color is string.
    * price_per_kg is float
    * weight is float
3. The name for all pepper objects should be "Pepper".
4. The price for all pepper objects should be the received <price_per_kg> * <weight>.
5. The pepper class has 2 PROTECTED attributes: color and weight.
6. The Pepper class implements the 3 abstract methods of Item:
    6.1 put_on_shelf - receives a single int parameter `shelf_id`, 
        prints the following message:
            Pepper is put on vegetable shelf #<shelf_id>.

         Where:
            * <shelf_id> - should be the received <shelf_id> parameter.
    6.2 get_department- receives no parameters and returns the string:
            VEGETABLE
    6.3 print_details - receives no parameters, prints data for the pepper:
            * The method prints the following text (note the line break):
                Item #<id> - <color> <name> belongs to the <department> department.
                It weights <weight> kg and costs <price> nis.

            * Where:
                * <id> - should be the item's id (use get_id method)
                * <color> - should be the <color> attribute (received in the constructor)
                * <name> - should be the item's department name (use get_department method)
                * <department> - should be the item's department name (use get_department method)
                * <weight> - should be the <weight> attribute (received in the constructor)
                * <price> - should be the item's price (use get_price method)

7. Make sure you add type hints and documentation to the class and to all its' methods!

---
Task 3.1
---
Create pepper.py file with the Pepper class according to the guidelines above.

"""

###################################
# Part 4 - Item ID
###################################
"""
In this task you will add the item's ID part.

The task is to make sure each item is created with a unique (int) ID,
and this id is generated automatically by the Item's class constructor.

---
Task 4.1
---
Change the constructor of Item so each item is created with a unique integer ID.
    IMPORTANT NOTES:
    - You are NOT allowed to add parameters to the constructor SIGNATURE!!
    - You must have an attribute "self._item_id" in class Item.
    - You can (and SHOULD) add static member to the Item class.
    - You can (and should) add code in the BODY of __init__ method (constructor) of Item.
"""

###################################
# Part 5 - HW1 main
###################################
"""
In this part you will create a small program that receives input from the user.
Based on the input the program will maintain a list of items - <grocery_store> list -
and will be able to print data on the list.

In every iteration - the program will ask the user for a command.

you will code this part in "hw1_main.py".

Note that the main loop and the program's skeleton were already written for you.
You have to fill the code based on the commands list below.

You will see the:
    # Your code goes here
comment in every place you need to add code.

Possible commands and what the program should do:
1. "add_milk" - 
    * The program will ask the user for the milk's price, with the following message:
        Please insert the price of the milk:
    * The program will ask the user for the milk's expiration date, with the following message:
        Please insert the expiration date of the milk:
    * The program will create a new milk with the received price and expiration date, 
      and will add it to the <grocery_store> list.

2. "add_pepper" - 
    * The program will ask the user for the pepper's color, with the following message:
        Please insert the color of the pepper:
    * The program will ask the user for the pepper's price per kg, with the following message:
        Please insert the pepper's price per KG:
    * The program will ask the user for the pepper's weight, with the following message:
        Please insert the pepper's weight:
    * The program will create a new pepper with the received color, price per KG and weight,
      and will add it to the <grocery_store> list.

3. "print" -
    * The program will print all the items in the list, using the "print_details" method.

4. "put_on_shelf" - 
    * The program will ask the user for the shelf id to use, with the following message:
        Please insert the shelf id:
    * The program will put all the items in the list on the shelf with the received shelf id,
      using the "put_on_shelf" method and the received shelf_id.

5. "total_value" - 
    * The program will print the TOTAL price of all the items in the <grocery_store> list:
        The total price is <total_price>.
        
        * Where:
            - <total_price> - is the TOTAL price of all the items in the <grocery_store> list.

5. "avg_value" - 
    * The program will print the AVERAGE price of all the items in the <grocery_store> list:
        The average price is <average_price>.
        
        * Where:
            - <average_price> - is the AVERAGE price of all the items in the <grocery_store> list.
                                with exactly 2 decimal points (for example - 23.46, 90.00, 32.87, 12.30, etc.)
    
    * If there are no items in the list, the program will print:
        No items in the store.

6. "remove" -
    * The program will ask the user for the id of the item to remove:
        Please insert the id of the item you want to remove:
    * If an item with such id exists in the <grocery_store> list, the program will remove it from the list,
      and will print:
        Item #<id> was removed from the list.
        
        * Where:
            - <id> - is the id of the removed item.
    * If an item with such id doesn't exist in the list, the program will print:
        Item #<id> was not found in the list.
        
        * Where:
            - <id> - is the id that was not found.

7. "exit" - 
    ALREADY DONE FOR YOU!
    * The program will break the loop.
8. Any other command - 
    ALREADY DONE FOR YOU!
    * The program will print an error message - and ask the user for a valid command.
"""

###################################
# GOOD LUCK
###################################
"""
GOOD LUCK!!!
"""
