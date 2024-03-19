from items.warehouse_item import WarehouseItem

class QueryBuilder(object):
    
    @staticmethod
    def search_by_name(search_str: str) -> str:
        query = "SELECT ID, NAME, CATEGORY FROM PRODUCTS WHERE PRODUCTS.NAME LIKE " + f"\"%{search_str}%\""
        return query