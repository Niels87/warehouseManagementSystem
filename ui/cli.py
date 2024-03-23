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
from ui.ui_state_machine import UIStateMachine
from ui.state_info import StateInfo

class CommandLineInterface(object):
    
    style_sheet = {
        "light_blue": "#00BFFF",
        "darker_blue": "#50A588",
        "red": "#FF0000",
    }
    
    def __init__(self) -> None:
        self._state_machine = UIStateMachine() 
        self._setup_prompt()
        

    @property
    def state_machine(self):
        return self._state_machine

    @state_machine.setter
    def state_machine(self, value):
        self._state_machine = value

    
    def _setup_prompt(self):
        # auto_completer = completion.FuzzyWordCompleter( 
        #     self._main_menu_options.keys()
        # )
        
        self._prompt_session = PromptSession(
            # completer=auto_completer,
            # complete_while_typing=True,
            # complete_style=CompleteStyle.COLUMN,
            
        )
    
    def on_startup(self):
        print("\nWelcome. What do you want to do?\n")
    
    def start(self):
        self.on_startup()
        self.state_machine.change_state("Main")
        self.main_loop()
    
    def main_loop(self):
        state_info = self.state_machine.state_info
        
        #self.print_start_menu()
        # print("You select options by typing their name.")
        # print("Automatic completions will be shown, when you start typing")
        user_input = self._print_prompt(state_info.text_above_prompt)
        state = self.state_machine.change_state(user_input)
        
        if state == "Exit":
            return
        else:
            self.main_loop()
    
    
    
    def _print_prompt(self, header: str):
        
        print_formatted_text(
            FormattedText([("#00BFFF",f"\n{header} ")])
            )
        _prompt_arrow = FormattedText([("#00BFFF","|> ")])
        return self._prompt_session.prompt(_prompt_arrow)
        
        
    # def print_start_menu(self):
        
    #     line = "------------------------"
    #     f_line = FormattedText([
    #         (self.style_sheet["darker_blue"],line)
    #     ])
                
    #     print_formatted_text(f_line)
    #     width = line.__len__()-1
    #     self._main_menu_options.keys()
            
    #     ws = "{" + f":<{width}"+ "}"
        
    #     for key in self._main_menu_options:
    #         option = self._main_menu_options[key].__name__.replace("_", " ").capitalize()
    #         s = f"| {key}"
    #         fs = ws.format(s) + "|"
    #         ffs = FormattedText([
    #             (self.style_sheet["darker_blue"], fs),
    #         ])
    #         print_formatted_text(ffs)
            
    #     print_formatted_text(f_line)


    
    
    
        