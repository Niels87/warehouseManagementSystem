from events.event_abs import EventABS
from events.request_status import RequestStatus
from items.warehouse_item import WarehouseItem

class AddItemRequest(EventABS):
    
    def __init__(self, item: WarehouseItem) -> None:
        super().__init__()
        self._item = item
        
    @property
    def item(self):
        return self._item
    

class AddItemResponse(EventABS):
    def __init__(self, request: AddItemRequest, status: RequestStatus) -> None:
        super().__init__()
        self._request = request
        self._status = status
        

    @property
    def request(self):
        return self._request

    @property
    def status(self):
        return self._status
