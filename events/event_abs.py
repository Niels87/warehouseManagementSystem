from event_handler import EventHandler
from abc import ABC, abstractmethod
import datetime
from uuid import uuid4
import inspect
from utils.event_debug import EventPosterDebugInfo
class EventABS(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        self._event_type = type(self)
        self._timestamp = datetime.datetime.now()
        self._id = self.timestamp.strftime("%d/%m/%Y_%H:%M:%S.%f_") + str(uuid4())
        
    @property
    def id(self):
        return self._id

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def event_type(self):
        return self._event_type

    def post(self):
        frame = inspect.currentframe().f_back
        
        debug_info = EventPosterDebugInfo(
            posting_class=frame.f_code.co_qualname,
            posting_file=frame.f_code.co_filename
        )
        EventHandler().post_event(self.event_type, self, debug_info)
        