from database.database_connection import DatabaseConnection
from event_system.events import add_item, event_abs, remove_item, search_database
from event_system.events.search_database import SearchDatabaseRequest, SearchDatabaseResponse
from event_system.events.add_item import AddItemRequest, AddItemResponse
from event_system.events.remove_item import RemoveItemRequest, RemoveItemResponse
from event_system.events.update_item import UpdateItemRequest, UpdateItemResponse
from event_system.event_handler import EventHandler
from event_system.events.event_abs import EventABS
from database.procedures import ProcedureArgumentsBuilder
from event_system.events import update_item


""" Calls stored procedures in the database, 
    when receiving database requests """
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
        proc_name = ProcedureArgumentsBuilder().get_procedure_name(request)
        proc_args = ProcedureArgumentsBuilder().get_arguments(request)
        result = self.db.call_stored_procedure(proc_name, proc_args)
        self.post_result(request, result)
        
    
    def post_result(self, request: event_abs.EventABS, result: list):
        match type(request):
            case search_database.SearchDatabaseRequest:
                SearchDatabaseResponse(result).post()
            case add_item.AddItemRequest:
                AddItemResponse(request, result).post()
            case remove_item.RemoveItemRequest:
                RemoveItemResponse(request, result).post()
            case update_item.UpdateItemRequest:
                UpdateItemResponse(request, result).post()