from events.event_abs import EventABS
from items.warehouse_item import WarehouseItem

class SearchDatabaseRequest(EventABS):
    
    def __init__(self, search_str: str) -> None:
        super().__init__()
        self._search_str = search_str
        
    @property
    def search_str(self):
        return self._search_str



class SearchDatabaseResponse(EventABS):
    
    def __init__(self, search_result: dict) -> None:
        super().__init__()
        self._search_result = search_result
        
    @property
    def search_result(self):
        return self._search_result