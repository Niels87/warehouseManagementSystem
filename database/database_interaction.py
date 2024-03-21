from database.database_connection import DatabaseConnection
from database.query_builder import QueryBuilder
from events.search_database import SearchDatabaseRequest, SearchDatabaseResponse
from events.add_item import AddItemRequest, AddItemResponse
from events.remove_item import RemoveItemRequest, RemoveItemResponse
from events.update_item import UpdateItemRequest, UpdateItemResponse
from event_handler import EventHandler
from events.event_abs import EventABS
from database.proc_args_builder import ProcArgsBuilder

class DatabaseInteraction(object):
    
    def __init__(self, db_connection: DatabaseConnection) -> None:
        self._db = db_connection
        EventHandler().subscribe_event(SearchDatabaseRequest, self.call_stored_procedure)
        EventHandler().subscribe_event(AddItemRequest, self.call_stored_procedure)
        EventHandler().subscribe_event(RemoveItemRequest, self.call_stored_procedure)
        EventHandler().subscribe_event(UpdateItemRequest, self.call_stored_procedure)
        
    @property
    def db(self):
        return self._db

        
    
    def call_stored_procedure(self, request: EventABS):
        proc_name = ProcArgsBuilder().get_proc_name(request)
        print("proc_name: " + str(proc_name))
        proc_args = ProcArgsBuilder().get_args(request)
        print("args: " + str(proc_args))
        result = self.db.query_database_procedure(proc_name, proc_args)
        return result
    
    def search_by_name(self, request: SearchDatabaseRequest):
        query = QueryBuilder().search_by_name(request.search_str)
        result = self.db.query_database(query)
        SearchDatabaseResponse(result).post()
    
    def add_item(self, request: AddItemRequest):
        query = QueryBuilder().add_new_item(request.item)
        result = self.db.query_database(query)
        AddItemResponse(request, result).post()
    
    def remove_item(self, request: RemoveItemRequest):
        query = QueryBuilder().remove_item(request.item)
        result = self.db.query_database(query)
        RemoveItemResponse(request, result).post()
    
    def update_item(self, request: UpdateItemRequest):
        query = QueryBuilder().update_item(request.item, request.update_field, request.new_value)
        result = self.db.query_database(query)
        UpdateItemResponse(request, result).post()
        
    