from not_in_use.item_category import ItemCategory
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

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
        
