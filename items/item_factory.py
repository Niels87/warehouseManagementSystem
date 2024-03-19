from items.warehouse_item import WarehouseItem


class WarehouseItemFactory(object):
    
    @staticmethod
    def create_item_from_database(db_info: dict) -> WarehouseItem:
        return WarehouseItem(
            id=db_info["id"],
            name=db_info["prod_name"],
            category=db_info["category"],
            price=db_info["price"],
            count=db_info["count"],
        )
    
    
