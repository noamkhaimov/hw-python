import abc


class Item(abc.ABC):
    """
    This class represents an item - which will be used in the store.
    """

    _ITEM_ID_GEN_CTR_ = None

    def __init__(self, name: str, price: float):
        """
        Constructor

        :param name: the name of the item
        :param price: the price of the item
        """
        ##########################
        # Do not change this part
        self._name = name
        self._price = price
        ##########################

        # PART 4: You can (and SHOULD) change the following line, and add more line(s) if needed.
        self._item_id = self._ITEM_ID_GEN_CTR_
        Item._ITEM_ID_GEN_CTR_ += 1

    def get_id(self) -> int:
        """
        Returns the item's id.

        :return: Returns the item's id.
        """
        return self._item_id

    def get_name(self) -> str:
        """
        Returns the item's name.

        :return: the item's name
        """
        return self._name

    def get_price(self) -> float:
        """
        Returns the item's price.

        :return: the item's price
        """
        return self._price

    @abc.abstractmethod
    def put_on_shelf(self, shelf_id: int) -> None:
        """
        Puts the item on the shelf.

        :param: shelf_id: the shelf id
        :return: None
        """
        pass

    @abc.abstractmethod
    def get_department(self):
        """
        Gets the Item's department.
        :return: Return a string that represents the item's department
        """
        pass

    @abc.abstractmethod
    def print_details(self):
        """
        Prints data for the item.
        :return: None
        """
        pass


