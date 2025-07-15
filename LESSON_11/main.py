"""
Module: main
This module defines a Kettle class that represents a kettle
with attributes for make, price, and operational state. 
It also demonstrates the creation and manipulation of Kettle objects.

Classes:
    Kettle: A class representing a Kettle with attributes for make, price, and operational state.
"""
class Kettle:
    """
    A class representing a Kettle with attributes for make, price, and operational state.

    Attributes:
        make (str): The brand or manufacturer of the kettle.
        price (float): The cost of the kettle.
        on (bool): The operational state of the kettle, where False
            indicates it is off and True indicates it is on.

    Methods:
        __init__(make: str, price: float) -> None:
            Initializes a Kettle object with the specified make
            and price, and sets the initial state to off.

        switch_on() -> None:
            Turns on the kettle by setting its 'on' attribute to True.
    """
    def __init__(self, make: str, price: float) -> None:
        self.make = make
        self.price = price
        self.on = False


    def switch_on(self) -> None:
        """
        Turns on the object by setting its 'on' attribute to True.

        This method modifies the state of the object to indicate that it is active or operational.
        """
        self.on = True


kenwood = Kettle("Kenwood", 8.90)

print(kenwood.price)
print(kenwood.make)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

hamilton.switch_on()
print(hamilton.on)

# kenwood.power: float = 1.5
# print(kenwood.power)
