from items.warehouse_item import WarehouseItem


class WarehouseItemFactory(object):
    
    @staticmethod
    def create_new_item_from_dict(db_info: dict) -> WarehouseItem:
        return WarehouseItem(
            id=db_info["ID"],
            name=db_info["name"],
            category=db_info["category"],
            price=db_info["price"],
            count=db_info["count"],
        )
    
    @staticmethod
    def create_new_item_from_tuple(db_info: tuple) -> WarehouseItem:
        return WarehouseItem(
            id=None,
            name=db_info[0],
            price=db_info[1],
            count=db_info[2],
            category=db_info[3],
        )
    

    @staticmethod
    def create_new_item_from_dict(db_info: dict) -> WarehouseItem:
        return WarehouseItem(
            id=None,
            name=db_info["name"],
            category=db_info["category"],
            price=db_info["price"],
            count=db_info["count"],
        )
    