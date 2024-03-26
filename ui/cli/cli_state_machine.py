from events import search_database, add_item, remove_item, update_item
from ui.cli.global_session_state import GlobalSessionState
from utils.singleton import Singleton
from ui.cli import states
class StateMachine(Singleton):
    
    def __init__(self) -> None:
        self._current_state = states.MainMenu()

    @property
    def current_state(self):
        return self._current_state

    def change_state(self, new_state: states.StateABS):
        self._current_state = new_state
    