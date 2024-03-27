from event_system.event_handler import EventHandler
from event_system.events.event_abs import EventABS
from event_system.events import search_database

class EventLogger(object):
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(search_database.SearchDatabaseRequest, self.log_event)
        EventHandler().subscribe_event(search_database.SearchDatabaseResponse, self.log_event)
    
    def log_event(self, event: EventABS):
        
        # maybe a match statement?
        
        print("logging event: " + event.id)
    
    