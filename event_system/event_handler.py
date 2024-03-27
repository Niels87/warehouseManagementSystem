from utils.singleton import Singleton
from collections import defaultdict
from typing import Type, Callable
from debug.event_debug import EventPosterDebugInfo
from prompt_toolkit import formatted_text, print_formatted_text

class EventHandler(Singleton):
    
    def __init__(self) -> None:
        pass

    debug_mode: bool = False
    
    _subscribers = defaultdict(list)

    # higher priority get called first
    def subscribe_event(self, event_type: type, fn: Callable, priority=0):
        self._subscribers[event_type].append((priority, fn))
        
        
    def unsubscribe_event(self, event_type: type, fn):
        try:
            self._subscribers[event_type].remove(fn)
        except:
            print("\n No such subscriber")
    
    def post_event(self, event_type: type, event_data, debug_info: EventPosterDebugInfo):
        if event_type in self._subscribers:
            for (priority, fn) in sorted(self._subscribers[event_type], key=lambda x: x[0], reverse=True):
                if self.debug_mode == True:
                    self.print_debug(event_type, priority, fn, debug_info)
                fn(event_data)
        else:
            pass #print("\nNo observers of type: " + str(event_type.__name__))
    
    def print_debug(self, event_type: type, priority: int, fn: Callable, debug_info: EventPosterDebugInfo ):
        f_text = formatted_text.FormattedText([
            ("#836363",f"{debug_info.posting_class} --> {event_type.__name__} --> ({priority}) {fn.__qualname__}")
        ])
        print_formatted_text(f_text)