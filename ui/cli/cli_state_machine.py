from events import search_database, add_item, remove_item, update_item
from ui.cli.state_info import StateInfo
from ui.cli.states import States
from ui.cli.session_history import History

class StateMachine():
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------
    
    def __init__(self) -> None:
        self._states = States().states
        self._transitions = self._init_transitions()
        self._current_state = "Start"
        self._state_info = StateInfo()
        self._session_history = History()
        

    @property
    def state_info(self):
        return self._state_info

    @state_info.setter
    def state_info(self, value):
        self._state_info = value

    @property
    def history(self):
        return self._session_history

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
    # @property
    # def state_info(self):
    #     try:
    #         return self.states[self.current_state]
    #     except:
    #         return StateInfo()
    
    def _init_transitions(self) -> dict:
        return {
            "Main": self.main_menu,
            #"Return": self.return_to_main,
            "Search": self.search,
            "Add": self.add_item,
            "Interact": self.interact_with_search_results,
            "Remove": self.remove_item,
            "Update": self.update_item,
            "Edit": self.edit_item,
        }
    
    ''' Check if input corresponds to a state, if it does,
        set the current state, then return the current states'''
    def change_state(self, new_state: str) -> str:
        if self.states.__contains__(new_state.capitalize()):
            self.current_state = new_state
            self.state_info = self.states[self.current_state]
        else:
            print(f"Command < {new_state} > not recognized")  
        return self.current_state
        
    
#-----------------------------------------------------
    
    
    def main_menu(self, user_input: str):
        return self.change_state(user_input)
    
    def search(self, user_input: str):
        
        search_database.SearchDatabaseRequest(search_str=user_input).post()
        self.change_state("Interact")
        self.state_info.set_autocompletions(self.history.get_names_in_last_search())
        return self.current_state
        
    def add_item(self, user_input: str):
        print("We are still working on the add_item functionality...")
        return self.change_state("Main")
    
    def interact_with_search_results(self, user_input: str):
        item = self.history.get_item_in_last_search(user_input)
        self.history.set_active_item_edit(item)
        return self.change_state("Edit")
    
    def edit_item(self, user_input: str):
        return self.change_state(user_input)
  
    def remove_item(self, user_input: str):
        if user_input == "Yes":
            remove_item.RemoveItemRequest(self.history.get_active_item_edit()).post()
            return self.change_state("Main")
        elif user_input == "No":
            return self.change_state("Main")
        else:
            print(f"{user_input} not recognized, try again")
            return self.current_state

    
    def update_item(self, user_input: str):
        
        pass
    
    # def return_to_main(self):
    #     self.current_state = "Main"            
        
    # def exit(self, user_input: str):
    #     return "Exit"
