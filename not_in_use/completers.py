from typing import Iterable
from prompt_toolkit.completion import Completer, Completion, FuzzyWordCompleter
from prompt_toolkit.completion.base import CompleteEvent
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import FormattedText

"""Custom autocompleter used to simulate menu behavior"""
class MenuCompleter(FuzzyWordCompleter):
    
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        
        for word in self.words:
            yield Completion(
                word,
                start_position=-20,   
                display=FormattedText([("#00BFFF",word)]),
                style='bg:#303030 fg:#8080A0'
            )

"""Custom autocompleter used to select among search results"""
class SearchResultCompleter(FuzzyWordCompleter):
    
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
    
        for word in self.words:
            yield Completion(
                word,
                start_position=-20,   
                display=FormattedText([("#00BFFF",word)]),
                style='bg:#303030 fg:#8080A0'
            )
        