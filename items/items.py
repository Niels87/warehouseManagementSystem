from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

"""
An item in the warehouse. Instantiate using the WarehouseItemFactory.
Based on data from the database. Typically from a SearchDatabaseRequest
"""
class WarehouseItem(object):
    
    def __init__(
        self, 
        id: int, 
        name: str,
        category: str,
        price: float,
        count: int
        ):
        self._id = id
        self._name = name
        self._category = category
        self._price = price
        self._count = count

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def price(self):
        return self._price

    @property
    def count(self):
        return self._count

        
    def print(self):
        blue = "#00BFFF"
        light_grey = "#D3D3D3"
        name = FormattedText([
            ("#00BFFF", f" {self.name}  "),
            ("#90EE90", " $ "),
            ("#D3D3D3", f"{str(self.price)}\n"),
            ("#D3D3D3", f"{self.category} | {str(self.count)}"),
        ])
        
        print_formatted_text(name)
    
    def get_formatted_text(self, nr: int):
        blue = "#00BFFF"
        light_grey = "#D3D3D3"
        name = FormattedText([
            ("#D3D3D3", f" {nr}"),
            ("#00BFFF", f" {self.name}  "),
            ("#90EE90", " $ "),
            ("#D3D3D3", f"{str(self.price)}\n"),
            ("#D3D3D3", f"{self.category} | {str(self.count)}"),
        ])
        
        print_formatted_text(name)
        

"""
A new item not yet added to the database. 
Used to send data provided by a user to the DatabaseHandler, 
from the CommandLineInterface, inside an AddItemRequest.
id = None, since the id will be generated by the database.
Instantiate with the WarehouseItemFactory.
"""
class NewWarehouseItem(WarehouseItem):
    
    def __init__(self, name: str, category: str, price: float, count: int):
        id = None
        super().__init__(id, name, category, price, count)