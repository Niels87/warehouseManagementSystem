from collections import defaultdict
from typing import Type

class EventHandler(object):
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------
    
    _subscribers = defaultdict(list)


    def subscribe_event(self, event_type: type, fn):
        self._subscribers[event_type].append(fn)
        
    
    def unsubscribe_event(self, event_type: type, fn):
        try:
            self._subscribers[event_type].remove(fn)
        except:
            print("\n No such subscriber")
    
    def post_event(self, event_type: type, event_data):
        if event_type in self._subscribers:
            for fn in self._subscribers[event_type]:
                fn(event_data)
        else:
            print("\nNo event of type: " + str(event_type))