from items.warehouse_item import WarehouseItem

class QueryBuilder(object):
    
    @staticmethod
    def search_by_name(search_str: str) -> str:
        query = "SELECT ID, NAME, CATEGORY, PRICE, COUNT FROM PRODUCTS WHERE PRODUCTS.NAME LIKE " + f"\"%{search_str}%\""
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
        query = (
            f"DELETE FROM products WHERE ID = {item.id};"
        )
        return query
    
    @staticmethod
    def update_item(item: WarehouseItem, field: str, new_value) -> str:
        if type(new_value) == str:
            query = (
                f"UPDATE products SET {field}=\"{new_value}\" WHERE ID = {item.id};"
            )
        else:            
            query = (
                f"UPDATE products SET {field}={new_value} WHERE ID = {item.id};"
            )
        return query