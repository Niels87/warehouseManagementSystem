from events.search_database import SearchDatabaseRequest, SearchDatabaseResponse
from event_handler import EventHandler

class SearchPrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(SearchDatabaseRequest, self.print_request)
        EventHandler().subscribe_event(SearchDatabaseResponse, self.print_response)
        
    
    
    def print_request(self, request: SearchDatabaseRequest):
        print("You searched for: " + request.search_str)
        
    def print_response(self, response: SearchDatabaseResponse):
        print("Search results:")
        
        for result in response.search_result[0]:
            print(str(result))
        