from prompt_toolkit.widgets import Label, TextArea, Frame
from prompt_toolkit.layout.containers import VSplit, HSplit, Window
from prompt_toolkit.application import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import PromptSession
import prompt_toolkit.buffer
import prompt_toolkit.input
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Float, FloatContainer, HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.shortcuts import print_container


class WareApp(object):
    
    kb = KeyBindings()
    
    def __init__(self) -> None:
        self.build_layout()
        
    
    def build_layout(self):
        # menu_completer = WordCompleter([
        #     "Search",
        #     "Add new item",
        #     "Remove item",
        #     "Update item",
        #     "Cancel",
        # ])
        
        ftext = FormattedText([
            ("#00BFFF", " SomeFormattedTextIwrote \n"),
            ("#00BFFF", " SomeOtherFormattedTextIwrote "),
            ("#00BFFF", " SomeOtherFormattedTextIwrote "),
            ("#00BFFF", " SomeOtherFormattedTextIwrote "),
            ("#00BFFF", " SomeOtherFormattedTextIwrote "),
            
        ])
        #buff = Buffer(completer=menu_completer, complete_while_typing=True)
        win = Window(
            FormattedTextControl(
                ftext
            )
        )
        frame = Frame(
            win
        )
        
        body = VSplit([
            frame,
            frame
        ])
        
        print_container(body)
        
        #self._app = Application(layout=Layout(body), key_bindings=self.kb)
        
    


def main():
    wapp = WareApp()
    #wapp._app.run()
    
if __name__ == "__main__":
    main()