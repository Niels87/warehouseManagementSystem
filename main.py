from database.database_handler import DatabaseHandler
from ui.response_printer import ResponsePrinter
from ui.request_printer import RequestPrinter
from items.warehouse_item import WarehouseItem
from events.add_item import AddItemRequest
from events.remove_item import RemoveItemRequest
from events.update_item import UpdateItemRequest
from ui.cli import CommandLineInterface


def main():
    
    db_config = {
        "db_name": "warehousedb",
        "sql_folder": "database/db_config/",
        "create_tables": "create_tables.sql",
        "create_procedures": "create_stored_procedures.sql",
        "delimiter": "--#--new--#", # delimiter for parsing sql-files
    }    
    
    setup(db_config)
        
    cli = CommandLineInterface()
    cli.start_menu()
    

def setup(config):
    
    db_handler = DatabaseHandler(config)
    db_handler.create_database()
    db_handler.initialize_database()
    
    simulate_previous_actions()
    
    RequestPrinter()
    ResponsePrinter()
    
def dismantle_session():
    DatabaseHandler().drop_database()


def simulate_previous_actions():
    item = WarehouseItem(1, "bla bla", "primedog", 78.2, 12)
    AddItemRequest(item).post()
    AddItemRequest(item).post()
    UpdateItemRequest(item, "name", "hejs").post()

main()