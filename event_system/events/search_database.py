from event_system.events.event_abs import EventABS
from items.items import WarehouseItem
from items.item_factory import WarehouseItemFactory

class SearchDatabaseRequest(EventABS):
    
    def __init__(self, search_str: str, field: str = "name") -> None:
        super().__init__()
        self._search_str = search_str
        self._field = field

    @property
    def field(self):
        return self._field
        
    @property
    def search_str(self):
        return self._search_str



class SearchDatabaseResponse(EventABS):
    
    def __init__(self, search_result: list) -> None:
        super().__init__()
        self._search_result = self._package_results(search_result)
        
    @property
    def search_result(self):
        return self._search_result
    
    def _package_results(self, search_result: list) -> list[WarehouseItem]:
        items = []
        for r in search_result:
            items.append(
                WarehouseItemFactory().create_item_from_dict(r)
            )
        return items