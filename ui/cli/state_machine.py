from utils.singleton import Singleton
from ui.cli import statemachine_states

"""
Accesspoint for the CLI to the statemachine
"""
class StateMachine(Singleton):
    
    def __init__(self) -> None:
        self._current_state = statemachine_states.MainMenu()

    @property
    def current_state(self):
        return self._current_state

    def change_state(self, new_state: statemachine_states.StateABS):
        self._current_state = new_state
        

    
    