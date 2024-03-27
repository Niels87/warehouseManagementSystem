from prompt_toolkit import PromptSession
import prompt_toolkit
import prompt_toolkit.layout
import prompt_toolkit.widgets
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.completion.word_completer import WordCompleter
from prompt_toolkit import completion
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.application import get_app, Application

from event_system.events import update_item
from event_system.events import add_item, remove_item, search_database

class CommandLineInterface(object):
    
    style_sheet = {
        "light_blue": "#00BFFF",
        "darker_blue": "#50A588",
        "red": "#FF0000",
        
    }
    
    def __init__(self) -> None:
        self._main_menu_options = {
            "Search": self.search,
            "Add new item": self.add_item,
            "Remove item": self.remove_item,
            "Update item": self.update_item,
            "Cancel": self.exit,
            }
        self._setup_prompt()
        
    
    
    def start(self):
        self.on_startup()
        self.start_menu()
    
    def start_menu(self):
        self.print_start_menu()
        print("You select options by typing their name.")
        print("Automatic completions will be shown, when you start typing")
        option = self._print_prompt("Main menu:")
        
        if option in self._main_menu_options:
            self._main_menu_options[option]()
        else:
            print("Choice not recognized, please chose one of the available options.")
            self.start_menu()
                
                
    def search(self):
        search_str = self._print_prompt("What do you want to search for?")
        search_database.SearchDatabaseRequest(search_str).post()
        
    
    def add_item(self):
        pass
    
    def remove_item(self):
        item_name = self._print_prompt("Name of the product you want to delete?")
        search_database.SearchDatabaseRequest(item_name).post()
        
    
    def update_item(self):
        pass
    
    def exit(self):
        pass
    
    
    def on_startup(self):
        print("\nWelcome. What do you want to do?\n")     
    
    def _setup_prompt(self):
        auto_completer = completion.FuzzyWordCompleter( 
            self._main_menu_options.keys()
        )
        
        self._prompt_session = PromptSession(
            completer=auto_completer,
            complete_while_typing=True,
            complete_style=CompleteStyle.COLUMN,
            
        )
        self._ta = prompt_toolkit.widgets.TextArea(prompt=self._prompt_session)
    
    def _print_prompt(self, header: str):
        
        print_formatted_text(
            FormattedText([("#00BFFF",f"\n{header} ")])
            )
        _prompt_arrow = FormattedText([("#00BFFF","|> ")])
        return self._prompt_session.prompt(_prompt_arrow)
        
    def print_start_menu(self):
        
        line = "------------------------"
        f_line = FormattedText([
            (self.style_sheet["darker_blue"],line)
        ])
                
        print_formatted_text(f_line)
        width = line.__len__()-1
        self._main_menu_options.keys()
            
        ws = "{" + f":<{width}"+ "}"
        
        for key in self._main_menu_options:
            option = self._main_menu_options[key].__name__.replace("_", " ").capitalize()
            s = f"| {key}"
            fs = ws.format(s) + "|"
            ffs = FormattedText([
                (self.style_sheet["darker_blue"], fs),
            ])
            print_formatted_text(ffs)
            
        print_formatted_text(f_line)


