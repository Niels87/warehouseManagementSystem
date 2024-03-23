from enum import Enum
from ui.state_info import StateInfo

class UIState(Enum):
    Update = StateInfo()
    Start = StateInfo()
    Main = StateInfo(
        text_above_prompt="Main menu:",
        transitions=["Search products", "Add new item", "Exit"],
    )
    Search = StateInfo(
        text_above_prompt="Search products by name"    
    )
    Add = StateInfo()
    Interact = StateInfo(
        transitions=["Remove item", "Update item", "Return", "Exit"]
    )
    Remove = StateInfo()
    Exit = StateInfo()