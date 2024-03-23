from events.add_item import AddItemRequest
from events.remove_item import RemoveItemRequest
from events.search_database import SearchDatabaseRequest
from events.update_item import UpdateItemRequest
from event_handler import EventHandler


class RequestPrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemRequest, self.print_add_item)
        EventHandler().subscribe_event(SearchDatabaseRequest, self.print_search_database)
        EventHandler().subscribe_event(RemoveItemRequest, self.print_remove_item)
        EventHandler().subscribe_event(UpdateItemRequest, self.print_update_item)
        
    def print_add_item(self, request: AddItemRequest):
        print( f"Request to add item: {request.item.name} to database..." )
                
    def print_remove_item(self, request: RemoveItemRequest):
        print( f"Request to remove item: {request.item.name} from database..." )
        
    def print_update_item(self, request: UpdateItemRequest):
        print( f"Request to update {request.update_field} of item: {request.item.name} to {request.new_value}..." )
    
    def print_search_database(self, request: SearchDatabaseRequest):
        #print("You searched for: " + request.search_str)
        pass