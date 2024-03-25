
from dataclasses import dataclass, field
from prompt_toolkit.formatted_text import FormattedText
from ui.cli.completers import MenuCompleter, SearchResultCompleter

@dataclass
class StateInfo:
    prompt_header: str = "Default text above prompt"
    escape_key_func: str = "return to main menu"
    
    # passed to an eval() inside the pre_run of a prompt-session
    pre_run: str = "self.prompt_session.default_buffer.start_completion"
    # Possible state transitions from this state.
    transitions: list[str] = field(default_factory=lambda: [])
    
    # Autocompletions
    autocompletions: list[str] = field(init=False)
    
    def __post_init__(self):
        self.autocompletions = self.transitions
        
    def set_autocompletions(self, completions: list[str]):
        self.autocompletions = completions
    
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