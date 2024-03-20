from events.add_item import AddItemResponse
from events.remove_item import RemoveItemResponse
from events.update_item import UpdateItemResponse
from events.search_database import SearchDatabaseResponse
from event_handler import EventHandler


class ResponsePrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemResponse, self.print_add_item)
        EventHandler().subscribe_event(SearchDatabaseResponse, self.print_search)
        EventHandler().subscribe_event(RemoveItemResponse, self.print_remove_item)
        EventHandler().subscribe_event(UpdateItemResponse, self.print_update_item)
        
    def print_add_item(self, response: AddItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} added succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        print("")
    
    def print_remove_item(self, response: RemoveItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} removed succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        print("")

    def print_update_item(self, response: UpdateItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} updated succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        
    
    def print_search(self, response: SearchDatabaseResponse):
        print("Search results:")
        for result in response.search_result[0]:
            print(str(result))
            
        print("")
        
        
            