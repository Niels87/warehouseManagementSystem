from items.item_category import ItemCategory


class WarehouseItem(object):
    
    def __init__(
        self, 
        id: int, 
        name: str,
        category: ItemCategory,
        price: float,
        count: int
        ):
        self._id = id
        self._name = name,
        self._category = category
        self._price = price
        self._count = count

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

        
    
    
        
