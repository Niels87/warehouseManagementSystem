from events.add_item import AddItemResponse
from events.remove_item import RemoveItemResponse
from events.update_item import UpdateItemResponse
from events.search_database import SearchDatabaseResponse
from event_handler import EventHandler
from prompt_toolkit import formatted_text, print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Label, TextArea, Frame, Box
from prompt_toolkit.layout.containers import VSplit, HSplit, Window, FloatContainer, WindowAlign
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Dimension
from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
from builtins import map
from prompt_toolkit.layout import HorizontalAlign
import os

"""
Prints responses from database request. 
For a search-request it prints the search results, 
formatted into a table. For the others it prints
warnings, if there were any, otherwise it indicates
a success.
"""
class ResponsePrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemResponse, self.print_add_item)
        EventHandler().subscribe_event(SearchDatabaseResponse, self.print_search_results)
        EventHandler().subscribe_event(RemoveItemResponse, self.print_remove_item)
        EventHandler().subscribe_event(UpdateItemResponse, self.print_update_item)
        
    def print_add_item(self, response: AddItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} added succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        print("")
    
    def print_remove_item(self, response: RemoveItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} removed succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        print("")

    def print_update_item(self, response: UpdateItemResponse):
        if response.warnings == None:
            print(f"{response.request.item.name} updated succesfully!")
        else:    
            for warning in response.warnings:
                print(warning)
        
        print("")
        
        
    """ It's a mess... I know... don't even try """
    def print_search_results(self, response: SearchDatabaseResponse):
        print("")
        
        if response.search_result.__len__() == 0:
            print("No products found")
            return
        
        nrs = [("#B3B3B3", f" \n\n")]
        names = [("#B3B3B3", f"name\n\n")]
        prices = [("#B3B3B3", f"price $\n\n")]
        counts = [("#B3B3B3", f"count\n\n")]
        categories = [("#B3B3B3", f"category\n\n")] 
        ids = [("#838383", f"id\n\n")] 
        
        nr = 0
        #combined_width = 0
        for result in sorted(response.search_result, key= lambda x: x.category):
            nr += 1
            
            nrs.append( ("#D3D3D3", f"{nr}\n") )
            names.append( ("#00BFFF", f"{result.name}\n") )
            prices.append( ("#63B363", f"{str(result.price)}\n") )
            counts.append( ("#BCBC8D", f"{str(result.count)}\n") )
            categories.append( ("#B3B3B3", f"{str(result.category)}\n") )
            ids.append( ("#838383", f"{result.id}\n") )
            
        
        info = [ nrs, names, prices, counts, categories, ids ]
        formatted = map(lambda x: FormattedText(x), info)
        ftc = map(lambda x: FormattedTextControl(x), formatted)
        wins = list(map(lambda x: Window(x,dont_extend_width=True), ftc))
        window_aligns = [
            WindowAlign.RIGHT,
            WindowAlign.LEFT,
            WindowAlign.RIGHT,
            WindowAlign.RIGHT,
            WindowAlign.LEFT,
            WindowAlign.CENTER,
            
        ]
        for win in wins:
            win.align = window_aligns.pop()
        
        
        body = VSplit( wins, align=HorizontalAlign.LEFT, padding=3)
        body.width = body.preferred_width( os.get_terminal_size().columns ).preferred
        inner_box = Box(body, padding_left=2, padding_right=2)
        frame = Frame(inner_box)
        box = Box(frame, padding_left=1)
        
        print_container(box)