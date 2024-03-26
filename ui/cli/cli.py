from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import completion
from prompt_toolkit.shortcuts import CompleteStyle
from ui.cli.cli_state_machine import StateMachine
from prompt_toolkit.key_binding import KeyBindings
from ui.cli.global_session_state import GlobalSessionState
from ui.cli import states

class CommandLineInterface(object):

    def __init__(self) -> None:
        self._state_machine = StateMachine()
        self._session_state = GlobalSessionState()
        self._init_prompt()
        self._init_escape_commands()
        
    @property
    def state_machine(self):
        return self._state_machine
    
    @property
    def prompt_session(self):
        return self._prompt_session    
    
    def start(self):
        self.on_startup()
        self.main_loop()
    
    def on_startup(self):
        print("\nWelcome. What do you want to do?\n")
    
    def main_loop(self):
        
        while True:       
            user_input = self._display_prompt()
            print("")
            if user_input == self._exit_command:
                print("Exiting application...")
                break
            if user_input == self._return_command:
                print("Returning to main menu...")
                self.state_machine.change_state(states.MainMenu())
            new_state = self.state_machine.current_state.state_action(user_input)
            self.state_machine.change_state(new_state)
            
            
    
    
    def _display_prompt(self):

        self.prompt_session.completer = self._make_auto_completer()
        
        print("")
        print_formatted_text(self.state_machine.current_state.format_escape_key_func())
        print_formatted_text(self.state_machine.current_state.format_header())
        
        _prompt_arrow = FormattedText([("#00BFFF"," |> ")])
        return self._prompt_session.prompt(
            message=_prompt_arrow,
            pre_run=eval(self.state_machine.current_state.pre_run),
        )
    
    
    
    def _init_prompt(self):
        
        self._init_key_bindings()
        self._prompt_session = PromptSession(
            complete_while_typing=True,
            complete_style=CompleteStyle.COLUMN,
            key_bindings=self._key_bindings
        )
    
    

    def _make_auto_completer(self) -> completion.FuzzyWordCompleter:
        return completion.FuzzyWordCompleter(self.state_machine.current_state.autocompletions)        
    
    def _init_key_bindings(self):
        self._key_bindings = KeyBindings()
        self._key_bindings.add('escape')(self._escape_key_pressed())
    
    def _init_escape_commands(self):
        self._exit_command = "###Exit###"
        self._return_command = "###Return###"
    
    def _escape_key_pressed(self):
        def handler(event):
            if type(self.state_machine.current_state) == states.MainMenu:
                self.prompt_session.app.exit(self._exit_command)
            else:
                self.prompt_session.app.exit(self._return_command)
        return handler
    