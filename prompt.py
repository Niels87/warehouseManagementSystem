from prompt_toolkit import PromptSession
import prompt_toolkit
import prompt_toolkit.layout
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.completion.word_completer import WordCompleter
from prompt_toolkit import completion
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.application import get_app, Application

from events import search_database, add_item, remove_item, update_item

class CommandLineInterface(object):
    
    
    def __init__(self) -> None:
        self._main_menu_options = {
            "Search by name": self.search,
            "Add new item": self.add_item,
            "Remove item": self.remove_item,
            "Update item": self.update_item,
            "Cancel": self.exit,
            }
        self._setup_prompt()
    
    def _setup_prompt(self):
        auto_completer = completion.FuzzyWordCompleter( 
            self._main_menu_options.keys()
        )
        
        self._prompt_session = PromptSession(
            completer=auto_completer,
            complete_while_typing=True,
            complete_style=CompleteStyle.COLUMN,
            
        )
    
    def _print_prompt(self, header: str):
        
        print_formatted_text(
            FormattedText([("#00BFFF",f"\n{header} ")])
            )
        _prompt_arrow = FormattedText([("#00BFFF","|> ")])
        return self._prompt_session.prompt(_prompt_arrow)
        
    
    def print_start_menu(self):
        
        line = FormattedText([
            ("#AFEEEE ","----------------------------------------")
        ])

        
        print("\nWelcome. What do you want to do?")
        
        print_formatted_text("\n" + line)
        width = line.__len__()-1
        self._main_menu_options.keys()
            
        ws = "{" + f":<{width}"+ "}"
        
        for key in self._main_menu_options:
            option = self._main_menu_options[key].__name__.replace("_", " ").capitalize()
            s = f"| {key}"
            fs = ws.format(s) + "|"
            print(fs)
        print_formatted_text(line + "\n")
        
    
    def start_menu(self):
    
        option = self._print_prompt("Main menu:")
        
        if option in self._main_menu_options:
            self._main_menu_options[option]()
        else:
            print("Choice not recognized, please chose one of the available options.")
            self.start_menu()
                
    def search(self):
        search_str = self._print_prompt("What do you want to search for?")
        search_database.SearchDatabaseRequest(search_str).post()
        self.start_menu()
        
    
    def add_item(self):
        pass
    
    def remove_item(self):
        pass
    
    def update_item(self):
        pass
    
    def exit(self):
        pass
    
    
    

