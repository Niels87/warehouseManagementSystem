from app import WarehouseApp

def main():
    
    db_config = {
        "db_name": "warehousedb",
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