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

    # higher priority get called first
    def subscribe_event(self, event_type: type, fn, priority=0):
        self._subscribers[event_type].append((priority, fn))
        
    
    def unsubscribe_event(self, event_type: type, fn):
        try:
            self._subscribers[event_type].remove(fn)
        except:
            print("\n No such subscriber")
    
    def post_event(self, event_type: type, event_data):
        if event_type in self._subscribers:
            for fn in sorted(self._subscribers[event_type], key=lambda x: x[0], reverse=True):
                fn[1](event_data)
        else:
            pass #print("\nNo observers of type: " + str(event_type.__name__))