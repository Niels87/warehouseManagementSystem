from event_system.events.add_item import AddItemRequest
from event_system.events.remove_item import RemoveItemRequest
from event_system.events.search_database import SearchDatabaseRequest
from event_system.events.update_item import UpdateItemRequest
from event_system.event_handler import EventHandler


class RequestPrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemRequest, self.print_add_item, priority=10)
        #EventHandler().subscribe_event(SearchDatabaseRequest, self.print_search_database, priority=10)
        EventHandler().subscribe_event(RemoveItemRequest, self.print_remove_item, priority=10)
        EventHandler().subscribe_event(UpdateItemRequest, self.print_update_item, priority=10)
        
    def print_add_item(self, request: AddItemRequest):
        print( f"Requesting to add item: {request.item.name} to database..." )
                
    def print_remove_item(self, request: RemoveItemRequest):
        print( f"Requesting to remove item: {request.item.name} from database..." )
        
    def print_update_item(self, request: UpdateItemRequest):
        print( f"Requesting to update {request.update_field} of item: {request.item.name} to {request.new_value}..." )
    
    def print_search_database(self, request: SearchDatabaseRequest):
        print("You searched for: " + request.search_str)
        pass
