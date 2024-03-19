from database.database_connection import DatabaseConnection
from database.query_builder import QueryBuilder
from events.search_database import SearchDatabaseRequest, SearchDatabaseResponse
from event_handler import EventHandler

class DatabaseHandler(object):
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------

    def __init__(self) -> None:
        self._db = DatabaseConnection()
        EventHandler().subscribe_event(SearchDatabaseRequest, self.search_by_name)

    @property
    def db(self):
        return self._db
        
    def search_by_name(self, request: SearchDatabaseRequest):
        query = QueryBuilder().search_by_name(request.search_str)
        result = self.db.query_database(query)
        SearchDatabaseResponse(result).post()
        
    # def search_by_name_procedure(self, request: SearchDatabaseRequest):
    #     query = QueryBuilder().search_by_name(request.search_str)
    #     self.db.
    #     result = self.db.query_database(query)
    #     SearchDatabaseResponse(result).post()
    