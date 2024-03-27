from app import WarehouseApp


"""
Run this to run the application.
It builds the database and tables, then sets up stored procedures.
It then adds items to the database, using the same procedures a 
user would (stored procedure add_item). 
It then starts the application. 
At the end it drops the whole database by calling the dismantle 
session function. This is obviously just for convenience when trying it out.
"""
def main():
    
    db_config = {
        "db_name": "warehousedb",
        "host": "localhost",
        "user": "root",
        "password": "Kom12345",
        "sql_folder": "database/db_config/",
        "create_tables": "create_tables.sql",
        "create_procedures": "create_stored_procedures.sql",
        "delimiter": "--#--new--#", # delimiter for parsing sql-files
    }
    
    # if True, prints event-chains from the eventsystem to console
    debug_mode = False

    app = WarehouseApp(db_config, debug_mode)
    app.run() 
       
    app.dismantle_session()
    
main()