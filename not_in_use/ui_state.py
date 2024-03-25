from enum import Enum
from ui.state_info import StateInfo

class UIState(Enum):
    Update = StateInfo()
    Start = StateInfo()
    Main = StateInfo(
        prompt_header="Main menu:",
        transitions=["Search products", "Add new item", "Exit"],
    )
    Search = StateInfo(
        prompt_header="Search products by name"    
    )
    Add = StateInfo()
    Interact = StateInfo(
        transitions=["Remove item", "Update item", "Return", "Exit"]
    )
    Remove = StateInfo()
    Exit = StateInfo()