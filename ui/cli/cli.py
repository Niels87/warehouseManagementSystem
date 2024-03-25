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
from ui.cli.cli_state_machine import StateMachine
from ui.cli.state_info import StateInfo
from ui.cli.completers import MenuCompleter
from prompt_toolkit.key_binding import KeyBindings
from event_handler import EventHandler
from events.search_database import SearchDatabaseResponse


class CommandLineInterface(object):

    def __init__(self) -> None:
        self._state_machine = StateMachine()
        self._init_prompt()
        self._init_escape_commands()
        
    @property
    def state_machine(self):
        return self._state_machine
    
    @property
    def prompt_session(self):
        return self._prompt_session    
    
    def on_startup(self):
        print("\nWelcome. What do you want to do?\n")
    
    def start(self):
        self.on_startup()
        self.state_machine.change_state("Main")
        self.main_loop()
    
    def main_loop(self):
       
        user_input = self._display_prompt()
        if user_input == self._exit_command:
            print("Exiting application...")
            return
        if user_input == self._return_command:
            print("Returning to main menu...")
            self.state_machine.change_state("Main")
            user_input = "Main"
        
        state = self.state_machine.current_state
        state_output = self.state_machine.transitions[state](user_input)
        self.main_loop()
    
    
    def _display_prompt(self):
        
        self.prompt_session.completer = self._make_auto_completer()
        
        print("")
        print_formatted_text(self.state_machine.state_info.format_escape_key_func())
        print_formatted_text(self.state_machine.state_info.format_header())
        
        _prompt_arrow = FormattedText([("#00BFFF"," |> ")])
        return self._prompt_session.prompt(
            message=_prompt_arrow,
            pre_run=eval(self.state_machine.state_info.pre_run),
        )
    
    
    def _escape_key_pressed(self):
        def handler(event):
            if self.state_machine.current_state == "Main":
                self.prompt_session.app.exit(self._exit_command)
            else:
                self.prompt_session.app.exit(self._return_command)
        return handler
    
    def _init_escape_commands(self):
        self._exit_command = "###Exit###"
        self._return_command = "###Return###"
    
    def _init_prompt(self):
        
        self._init_key_bindings()
        auto_completer = self._make_auto_completer()
        
        self._prompt_session = PromptSession(
            completer=auto_completer,
            complete_while_typing=True,
            complete_style=CompleteStyle.COLUMN,
            key_bindings=self._key_bindings
        )
    
    def _init_key_bindings(self):
        self._key_bindings = KeyBindings()
        self._key_bindings.add('escape')(self._escape_key_pressed())


    def _make_auto_completer(self) -> completion.FuzzyWordCompleter:
        state_info = self.state_machine.state_info
        # menu_completer = MenuCompleter(state_info.autocompletions)
        # return menu_completer
        return completion.FuzzyWordCompleter(state_info.autocompletions)
        
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


    
    
    
        