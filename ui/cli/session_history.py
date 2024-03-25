from events.search_database import SearchDatabaseResponse
from event_handler import EventHandler
from builtins import map
from items.warehouse_item import WarehouseItem

class History(object):
    
    def __init__(self) -> None:
        self._last_search = []
        EventHandler().subscribe_event(SearchDatabaseResponse, self._set_last_search)

    @property
    def last_search(self):
        return self._last_search

    @last_search.setter
    def last_search(self, value):
        self._last_search = value

    def _set_last_search(self, response: SearchDatabaseResponse):
        self.last_search = response.search_result

    def get_names_in_last_search(self) -> list[str]:
        names = list( map(lambda x: x.name , self.last_search) )
        return names
    
    def get_item_in_last_search(self, item_name: str) -> WarehouseItem:
        for item in self.last_search:
            if item.name == item_name:
                return item
        return None
    
    def set_active_item_edit(self, item: WarehouseItem ):
        self._active_edit = item
    
    def get_active_item_edit(self) -> WarehouseItem:
        return self._active_edit
        
    
    
    
    
    