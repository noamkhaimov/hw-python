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
        price = float(input("Please insert the price of the milk:"))
        """
        Receive expiration date
        """
        expiration_date = input("Please insert the expiration date of the milk:")
        """
        Create a new Milk object, and add it to the <grocery_store> list. 
        """
        grocery_store.append(Milk(price, expiration_date))
    elif command == "add_pepper":
        pass
        """
        Receive color from the user
        """
        color = input("Please insert the color of the pepper:")
        """
        Receive price_per_kg from the user
        """
        price_per_kg = float(input("Please insert the price per kg of the pepper:"))
        """
        Receive weight from the user
        """
        weight = float(input("Please insert the weight of the pepper:"))
        """
        Create a new Pepper object, and add it to the <grocery_store> list. 
        """
        grocery_store.append(Pepper(color, price_per_kg, weight))
    elif command == "print":
        pass
        """
        Prints all the items in the <grocery_store> list, using the "print_details" method.
        """
        for item in grocery_store:
            item.print_details()
    elif command == "put_on_shelf":
        pass
        """
        Receives shelf_id from the user
        """
        shelf_id = int(input("Please insert the shelf id:"))

        """
        Call `put_on_shelf` method with the received <shelf_id> for all the items in the list.
        """
        for item in grocery_store:
            item.put_on_shelf(shelf_id)
    elif command == "total_value":
        pass
        """
        Prints the TOTAL price of all the items in the <grocery_store> list.
        """
        print(sum([item.get_price() for item in grocery_store]))
    elif command == "avg_value":
        pass
        """
        Prints the AVERAGE price of all the items in the <grocery_store> list.
        """
        if grocery_store:
            avg_value = sum([item.get_price() for item in grocery_store]) / len(grocery_store)
            print(f"{avg_value:.2f}")
        else:
            print("No items in the store")
    elif command == "remove":
        pass
        """
        Receive the id of the item to remove from the user
        """
        id_to_remove = int(input("Please insert the id of the item you want to remove:"))
        for item in grocery_store:
            if item.get_id() == id_to_remove:
                grocery_store.remove(item)
                print(f"Item #{id_to_remove} has been removed.")
                break
            else:
                print(f"Item with id {id_to_remove} does not exist.")

        """
        If an item with the received id exists - remove the item.
        In any case - print an appropriate message.
        """
    elif command == "exit":
        break
    else:
        print(f"Sorry! The command {command} is unknown. Please try again.")

print("Thank you for using FUN in the GROCERY STORE!")
