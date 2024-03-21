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
from events.update_item import UpdateItemRequest
import prompt

def main():
    RequestPrinter()
    ResponsePrinter()  
    DatabaseConnection()
    DatabaseHandler()
    
    
    item = WarehouseItem(2, 'bla bla', 'primedog', 78.2, 12)
    
    #SearchDatabaseRequest("bla").post()
    AddItemRequest(item).post()
    #SearchDatabaseRequest("bla").post()
    AddItemRequest(item).post()
    #SearchDatabaseRequest("bla").post()
    #RemoveItemRequest(item).post()
    UpdateItemRequest(item, "price", 25.3).post()
    #SearchDatabaseRequest("bla").post()
    UpdateItemRequest(item, "name", "got a new name").post()
    #SearchDatabaseRequest("bla").post()
    
    
    cli = prompt.CommandLineInterface()
    cli.start_menu()
    



main()