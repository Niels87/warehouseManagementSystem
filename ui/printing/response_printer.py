from event_system.events.add_item import AddItemResponse
from event_system.events.remove_item import RemoveItemResponse
from event_system.events.update_item import UpdateItemResponse
from event_system.events.search_database import SearchDatabaseResponse
from event_system.event_handler import EventHandler
from ui.printing.formatted_printing import ItemPrinter


"""
Prints responses from database request. 
For a search-request it prints the search results, 
formatted into a table. For the others it prints
warnings, if there were any, otherwise it indicates
a success.
"""
class ResponsePrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemResponse, self.print_add_item)
        EventHandler().subscribe_event(SearchDatabaseResponse, self.print_search_results)
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
        
        print("")
        
        
    """ It's a mess... I know... don't even try """
    def print_search_results(self, response: SearchDatabaseResponse):
        
        if response.search_result.__len__() == 0:
            print("No products found")
            return
        
        ItemPrinter().print_table_of_items(response.search_result)