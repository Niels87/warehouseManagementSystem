from items.warehouse_item import WarehouseItem

class QueryBuilder(object):
    
    @staticmethod
    def search_by_name(search_str: str) -> str:
        query = "SELECT ID, NAME, CATEGORY FROM PRODUCTS WHERE PRODUCTS.NAME LIKE " + f"\"%{search_str}%\""
        return query
    
    @staticmethod
    def add_new_item(item: WarehouseItem) -> str:
        query = (
            f"INSERT INTO products ( NAME, category, price, count ) " 
            f"VALUES (\"{item.name}\", \"{item.category}\", {item.price}, {item.count});"
        )
        return query
    
    @staticmethod
    def remove_item(item: WarehouseItem) -> str:
        print("remove item query")
        query = (
            f"DELETE FROM products WHERE ID = {item.id};"
        )
        return query