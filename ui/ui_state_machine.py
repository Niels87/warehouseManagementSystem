from events import search_database, add_item, remove_item, update_item
from ui.state_info import StateInfo

class UIStateMachine():
    
    # # Singleton --------------------------------
    # _instances = {} # dict([cls, instance])

    # def __new__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         instance = super().__new__(cls)
    #         cls._instances[cls] = instance
    #     return cls._instances[cls]
    # # ------------------------------------------
    
    def __init__(self) -> None:
        self._states = self._init_states()
        self._transitions = self._init_transitions()
        self._current_state = "Start"

    @property
    def states(self):
        return self._states

    @property
    def transitions(self):
        return self._transitions

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, value):
        self._current_state = value
    
    # Try to get the info for the current state or return a default StateInfo    
    @property
    def state_info(self):
        try:
            return self.states[self.current_state]
        except:
            return StateInfo()
    
    def _init_states(self) -> dict:
        return {
            "Main": StateInfo(
                text_above_prompt="Main menu:",
                transitions=["Search products", "Add new item", "Exit"],
            ),
            "Search": StateInfo(
                text_above_prompt="Search products by name"    
            ),
            "Add": StateInfo(
                text_above_prompt="Add new item"
            ),
            # "Pick_from_search": StateInfo(
            #     text_above_prompt="Pick a product"
            # ),
            "Interact": StateInfo(
                text_above_prompt="Select a product to interact with",
                transitions=["Update item", "Remove item", "Return", "Exit"]
            ),
            "Remove": StateInfo(),
            "Update": StateInfo(),
            "Exit": StateInfo(),
        }
    
    def _init_transitions(self) -> dict:
        return {
            "Main": self.main_menu,
            "Return": self.main_menu,
            "Search": self.search,
            "Add": self.add_item,
            "Interact": self.interact_with_search_results,
            "Remove": self.remove_item,
            "Update": self.update_item,
            "Exit": self.exit,
        }
    
    ''' Try to get the function from the transition dictionary,
        otherwise return the current transition'''
    def change_state(self, new_state: str) -> str:
        
        try:
            self.transitions[new_state.capitalize()]()
        except:
            #self.transitions[self.current_state]()
            print(f"State transition < {new_state} > not recognized")
        
        print(self.current_state)
        return self.current_state
        
    
#-----------------------------------------------------
    
    
    def main_menu(self):
        self.current_state = "Main"
    
    def search(self):
        self.current_state = "Search"
        
    def add_item(self):
        self.current_state = "Add"
    
    def interact_with_search_results(self):
        self.current_state = "Interact"
  
    def remove_item(self):
        self.current_state = "Remove"         
    
    def update_item(self):
        self.current_state = "Update"
    
    def exit(self):
        self.current_state = "Exit"
