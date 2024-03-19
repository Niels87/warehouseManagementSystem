from event_handler import EventHandler
from abc import ABC, abstractmethod
import datetime
from uuid import uuid4

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
        #print("Post: " + self.event_type.__name__ + " - " + self.timestamp.strftime("%d/%m/%y-%H:%M:%S"))
        EventHandler().post_event(self.event_type, self)
        