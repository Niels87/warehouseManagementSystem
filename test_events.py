from event_handler import EventHandler
from events.search_database import SearchDatabaseResponse, SearchDatabaseRequest
from event_logger import EventLogger
from database.query_builder import QueryBuilder
from database.database_connection import DatabaseConnection
from database.database_handler import DatabaseHandler
from search_print import SearchPrinter

def main():
        
    EventLogger()
    DatabaseConnection()
    SearchPrinter()
    DatabaseHandler()
    
    search_str = "quantum"
    
    SearchDatabaseRequest(search_str).post()
    
    
    
    

    



main()