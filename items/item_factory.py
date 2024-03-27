from items.items import WarehouseItem, NewWarehouseItem


class WarehouseItemFactory(object):
    
    @staticmethod
    def create_item_from_dict(item_info: dict) -> WarehouseItem:
        return WarehouseItem(
            id=item_info["ID"],
            name=item_info["name"],
            category=item_info["category"],
            price=item_info["price"],
            count=item_info["count"],
        )
    
    @staticmethod
    def create_new_item_from_tuple(item_info: tuple) -> WarehouseItem:
        return WarehouseItem(
            id=None,
            name=item_info[0],
            price=item_info[1],
            count=item_info[2],
            category=item_info[3],
        )
    

    @staticmethod
    def create_new_item_from_dict(item_info: dict) -> NewWarehouseItem:
        return WarehouseItem(
            id=None,
            name=item_info["Name"],
            category=item_info["Category"],
            price=item_info["Price"],
            count=item_info["Count"],
        )
    