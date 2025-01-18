from typing import List

from item import Item
from milk import Milk
from pepper import Pepper

###################################
# Part 0 - Personal Details
###################################
print("212711519")  # replace 123456789 with the id of the first student
print("Noam Khaimov")  # replace name1 with the name of the first student
print("noam.khaimov@gmail.com")  # replace name1@email.com with the email of the first student

###################################
# Part 5.1 - HW1 main
###################################

print("Welcome to advanced python course - HW 1 - FUN in the GROCERY STORE")

"""
The grocery store items list
"""
grocery_store: List[Item] = []

"""
The main loop
"""
while True:
    command = input("Please enter a command: ")

    if command == "add_milk":
        pass
        """
        Receive price
        """
        # Your code goes here

        """
        Receive expiration date
        """
        # Your code goes here

        """
        Create a new Milk object, and add it to the <grocery_store> list. 
        """
        # Your code goes here
    elif command == "add_pepper":
        pass
        """
        Receive color from the user
        """
        # Your code goes here

        """
        Receive price_per_kg from the user
        """
        # Your code goes here

        """
        Receive weight from the user
        """
        # Your code goes here

        """
        Create a new Pepper object, and add it to the <grocery_store> list. 
        """
        # Your code goes here
    elif command == "print":
        pass
        """
        Prints all the items in the <grocery_store> list, using the "print_details" method.
        """
        # Your code goes here
    elif command == "put_on_shelf":
        pass
        """
        Receives shelf_id from the user
        """
        # Your code goes here

        """
        Call `put_on_shelf` method with the received <shelf_id> for all the items in the list.
        """
        # Your code goes here
    elif command == "total_value":
        pass
        """
        Prints the TOTAL price of all the items in the <grocery_store> list.
        """
        # Your code goes here
    elif command == "avg_value":
        pass
        """
        Prints the AVERAGE price of all the items in the <grocery_store> list.
        """
        # Your code goes here
    elif command == "remove":
        pass
        """
        Receive the id of the item to remove from the user
        """
        # Your code goes here

        """
        If an item with the received id exists - remove the item.
        In any case - print an appropriate message.
        """
    elif command == "exit":
        break
    else:
        print(f"Sorry! The command {command} is unknown. Please try again.")

print("Thank you for using FUN in the GROCERY STORE!")
