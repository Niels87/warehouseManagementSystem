
from dataclasses import dataclass, field

@dataclass
class StateInfo:
    text_above_prompt: str = "Default text above prompt"
    transitions: list[str] = field(default_factory=lambda: ["Return", "Exit"])