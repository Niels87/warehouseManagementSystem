from database.database_connection import DatabaseConnection
from database.query_builder import QueryBuilder
from events.search_database import SearchDatabaseRequest, SearchDatabaseResponse
from events.add_item import AddItemRequest, AddItemResponse
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
        EventHandler().subscribe_event(AddItemRequest, self.add_item)
        
    @property
    def db(self):
        return self._db
        
    def search_by_name(self, request: SearchDatabaseRequest):
        query = QueryBuilder().search_by_name(request.search_str)
        print(query)
        result = self.db.query_database(query)
        SearchDatabaseResponse(result).post()
    
    def add_item(self, request: AddItemRequest):
        query = QueryBuilder().add_new_item(request.item)
        print(query)
        response = self.db.query_database(query)
        print(str(response))
        
        
    # def search_by_name_procedure(self, request: SearchDatabaseRequest):
    #     query = QueryBuilder().search_by_name(request.search_str)
    #     self.db.
    #     result = self.db.query_database(query)
    #     SearchDatabaseResponse(result).post()
    