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
import itertools
import database.database_builder as database_builder
from database.proc_args_builder import ProcArgsBuilder

def main():
    
    db_config = {
        "db_name": "warehousedb",
        "sql_folder": "database/db_config/",
        "create_tables": "create_tables.sql",
        "create_procedures": "create_stored_procedures.sql",
        "delimiter": "--#--new--#",
    }
    
    # db_conn = DatabaseConnection()
    # print("after db singleton")
    db_handler = DatabaseHandler(db_config)
    db_handler.create_database()
    db_handler.initialize_database()
    
    # setup_db.DatabaseBuilder().setup_database("database/queries")
    
    # RequestPrinter()
    # ResponsePrinter()  
    # DatabaseHandler()
    
    
    item = WarehouseItem(2, 'bla bla', 'primedog', 78.2, 12)
    
    # #SearchDatabaseRequest("bla").post()
    req = AddItemRequest(item).post()
    
    req2 = RemoveItemRequest(item).post()
    
    # #SearchDatabaseRequest("bla").post()
    # AddItemRequest(item).post()
    # #SearchDatabaseRequest("bla").post()
    # #RemoveItemRequest(item).post()
    # UpdateItemRequest(item, "price", 25.3).post()
    # #SearchDatabaseRequest("bla").post()
    # UpdateItemRequest(item, "name", "got a new name").post()
    # #SearchDatabaseRequest("bla").post()
    
    # setup_db.DatabaseBuilder().setup_database("database/queries")
    
    
    # mydb = DatabaseConnection().db
    # delimiter = "--#-new-query"
    # with open('database/queries/stored_procedures.sql', 'r') as f:
    #     queries = itertools.groupby(f, key= lambda x: x.lstrip().startswith(delimiter) )
    #     for k, v in queries:
    #         print("---")
            
    #         print(list(v))
    #         print(''.join(list(v)))
        # with mydb.cursor() as cursor:
            
        #     cursor.execute(f.read(), multi=True)
        # mydb.commit()
    
    # with mydb.cursor() as cursor:
    #     cursor.callproc('search_product_name', ('bla', ''))
    #     result = cursor.fetchall()
    #     print(result)
    #     for result in cursor.stored_results():
    #         print(result.fetchall())
    # cli = prompt.CommandLineInterface()
    # cli.start_menu()
    



main()