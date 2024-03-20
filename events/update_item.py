from events.event_abs import EventABS
from items.warehouse_item import WarehouseItem

class UpdateItemRequest(EventABS):
    
    def __init__(self, item: WarehouseItem, update_field: str, new_value) -> None:
        super().__init__()
        self._item = item
        self._update_field = update_field
        self._new_value = new_value

            
    @property
    def item(self):
        return self._item

    @property
    def update_field(self):
        return self._update_field

    @property
    def new_value(self):
        return self._new_value

    

        

class UpdateItemResponse(EventABS):
    def __init__(self, request: UpdateItemRequest, warnings: list[Warning]) -> None:
        super().__init__()
        self._request = request
        self._warnings = warnings
        

    @property
    def request(self):
        return self._request

    @property
    def warnings(self):
        return self._warnings