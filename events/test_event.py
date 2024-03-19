from events.event_abs import EventABS


class MyTestEvent(EventABS):
    
    def __init__(self, data: str) -> None:
        super().__init__()
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


        
    
    