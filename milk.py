from item import Item


class Milk(Item):
    """
    This class represents the milk - an item which inherit from Item class.
    """
    pass

    def __init__(self, price: float, expiration_date: str):
        """
        Constructor (Milk)

        :param price: Represents the price of the milk.
        :param expiration_date: Represents the expiration date of the milk.
        """
        super().__init__("MILK", price)
        self._expiration_date = expiration_date # todo check naming convention private/protected in all other as well

    def put_on_shelf(self, shelf_id: int) -> None:
        """
        Puts the milk item on the shelf. Print details of action.

        :param shelf_id: Represents the shelf id.
        :return: None
        """
        print(f"Milk carton is put in the fridge on shelf #{shelf_id}")

    def get_department(self) -> str:
        """
        Get the milk items department.
        :return: string "DAIRY"
        """

        return "DAIRY"

    def print_details(self):
        """
        Prints data for the milk item.
        :return: None
        """
        print(f"Item #{self.get_id()} - {self.get_name()} costs {self.get_price()} nis. It belongs to the {self.get_department()} department."
              f"Should be kept COLD, will expire on {self._expiration_date}.")



