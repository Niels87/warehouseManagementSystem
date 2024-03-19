from events.event_abs import EventABS
from items.warehouse_item import WarehouseItem

class RemoveItemRequest(EventABS):
    
    def __init__(self, item: WarehouseItem) -> None:
        super().__init__()
        self._item = item
        
    @property
    def item(self):
        return self._item

        

