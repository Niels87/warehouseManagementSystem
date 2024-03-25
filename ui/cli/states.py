from ui.cli.state_info import StateInfo
from dataclasses import dataclass, field
from prompt_toolkit.formatted_text import FormattedText

class States(object):

    def __init__(self) -> None:
        self._states = self._init_states()

    @property
    def states(self):
        return self._states
  
    def _init_states(self) -> dict:
        return {
            "Main": StateInfo(
                prompt_header="Main menu:",
                transitions=["Search", "Add"],
                escape_key_func = "exit the application"
                ),
            "Search": StateInfo(
                prompt_header="Search products by name",
                ),
            "Add": StateInfo(
                prompt_header="Add new item",
                ),
            "Interact": StateInfo(
                prompt_header="Select a product to interact with",
                pre_run="()"
                ),
            "Edit": StateInfo(
                prompt_header="What do you want to do?",
                transitions=["Remove", "Update"]                
                ),
            "Remove": StateInfo(
                prompt_header="Remove",
                transitions=["Yes", "No"]   # not technically transitions, just autocompletions, refactor?
                ),
            "Update": StateInfo(
                prompt_header="Update"
                ),
            "Exit": StateInfo(
                prompt_header="Exit"
                ),
        }
