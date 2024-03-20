from event_handler import EventHandler
from events.search_database import SearchDatabaseResponse, SearchDatabaseRequest
from event_logger import EventLogger
from database.query_builder import QueryBuilder
from database.database_connection import DatabaseConnection
from database.database_handler import DatabaseHandler
from search_print import SearchPrinter
from ui.response_printer import ResponsePrinter
from ui.request_printer import RequestPrinter
from items.warehouse_item import WarehouseItem
from events.add_item import AddItemRequest
from events.remove_item import RemoveItemRequest

def main():
    RequestPrinter()
    ResponsePrinter()  
    
    #EventLogger()
    DatabaseConnection()
    DatabaseHandler()
      
    
    # search_str = "quantum"
    
    # SearchDatabaseRequest(search_str).post()
    
    item = WarehouseItem(1, 'bla bla', 'primedog', 78.2, 12)
    
    SearchDatabaseRequest("bla").post()
    AddItemRequest(item).post()
    SearchDatabaseRequest("bla").post()
    AddItemRequest(item).post()
    SearchDatabaseRequest("bla").post()
    RemoveItemRequest(item).post()
    SearchDatabaseRequest("bla").post()
    

    



main()