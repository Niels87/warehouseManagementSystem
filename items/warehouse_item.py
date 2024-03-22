from not_in_use.item_category import ItemCategory


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
        print("name: " + self.name)
        print("category: " + self.category)
        print("price: " + str(self.price))
        print("count: " + str(self.count))
    
        
