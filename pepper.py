from item import Item


class Pepper(Item):
    """
    This class represents the pepper - an item which inherit from Item class.
    """
    def __init__(self, color: str, price_per_kg: float, weight: float):
        """
        Constructor (Pepper)
        :param color: The color of the pepper.
        :param price_per_kg: The price per kg of the pepper.
        :param weight: The weight of the pepper.
        """
        super().__init__("Pepper", price_per_kg * weight)
        self._color = color
        self._weight = weight

    def put_on_shelf(self, shelf_id: int) -> None:
        """
        Puts the pepper item on the vegetable shelf. Print details of action.
        :param shelf_id: Receive the shelf type.
        :return: None
        """
        print(f"Pepper is put on vegetable shelf #{shelf_id}")

    def get_department(self) -> str:
        """
        Gets the pepper's item department.
        :return: Return a string that represents the pepper's department.
        """
        return "VEGETABLE"

    def print_details(self) -> None:
        """
        Prints data for the pepper item.
        :return: None
        """
        print(f"Item #{self.get_id()} - {self._color} {self.get_department()} belongs to the {self.get_department()} department."
              f"It weights {self._weight} kg and costs {self.get_price()} nis.")




