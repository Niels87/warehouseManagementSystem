
from dataclasses import dataclass, field
from prompt_toolkit.formatted_text import FormattedText
from ui.cli.completers import MenuCompleter, SearchResultCompleter
from typing import Callable
from abc import ABC, abstractmethod


class StateABS(ABC):
    
    @abstractmethod
    def __init__(
            self, 
            prompt_header: str, 
            autocompletions: list[str],
            escape_key_func = "return to main menu",
            pre_run = "self.prompt_session.default_buffer.start_completion",
        ) -> None:

        self._prompt_header = prompt_header
        self._autocompletions = autocompletions
        self._escape_key_func = escape_key_func
        
        # passed to an eval() inside the pre_run of a prompt-session
        self._pre_run = pre_run

    @property
    def autocompletions(self):
        return self._autocompletions

    @property
    def prompt_header(self):
        return self._prompt_header

    @property
    def escape_key_func(self):
        return self._escape_key_func

    @property
    def pre_run(self):
        return self._pre_run

    @abstractmethod
    def state_action(self):
        pass
    
    
    def format_header(self) -> FormattedText:
        return FormattedText([
            ("#00BFFF",f"{self.prompt_header}")
        ])   
    
    def format_escape_key_func(self) -> FormattedText:
        return FormattedText([
            ("#495969", "Press "),
            ("#495969 italic", "escape "),
            ("#495969", f"to {self.escape_key_func}"),
        ])



# @dataclass
# class StateInfo:
#     state_action: Callable
#     prompt_header: str = "Default text above prompt"
#     escape_key_func: str = "return to main menu"
    
#     # passed to an eval() inside the pre_run of a prompt-session
#     pre_run: str = "self.prompt_session.default_buffer.start_completion"
#     # Possible state transitions from this state.
#     transitions: list[str] = field(default_factory=lambda: [])
    
#     # Autocompletions
#     autocompletions: list[str] = field(init=False)
    
#     def __post_init__(self):
#         self.autocompletions = self.transitions
        
#     def set_autocompletions(self, completions: list[str]):
#         self.autocompletions = completions
    
#     def format_header(self) -> FormattedText:
#         return FormattedText([
#             ("#00BFFF",f"{self.prompt_header}")
#             ])   
    
#     def format_escape_key_func(self) -> FormattedText:
#         return FormattedText([
#             ("#495969", "Press "),
#             ("#495969 italic", "escape "),
#             ("#495969", f"to {self.escape_key_func}"),
#         ])