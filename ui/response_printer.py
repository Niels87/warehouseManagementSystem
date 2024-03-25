from events.add_item import AddItemResponse
from events.remove_item import RemoveItemResponse
from events.update_item import UpdateItemResponse
from events.search_database import SearchDatabaseResponse
from event_handler import EventHandler
from prompt_toolkit import formatted_text, print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Label, TextArea, Frame, Box
from prompt_toolkit.layout.containers import VSplit, HSplit, Window, FloatContainer
from prompt_toolkit.application import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
from builtins import map
from prompt_toolkit.layout import HorizontalAlign
import os
class ResponsePrinter(object):
    
    def __init__(self) -> None:
        EventHandler().subscribe_event(AddItemResponse, self.print_add_item)
        EventHandler().subscribe_event(SearchDatabaseResponse, self.print_search)
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
        
        
    """It's a mess... I know... don't even try """
    def print_search(self, response: SearchDatabaseResponse):
        print("")
        
        if response.search_result.__len__() == 0:
            print("No products found")
            return
        
        nrs = [("#D3D3D3", f" \n")]
        names = [("#D3D3D3", f"name\n")]
        prices = [("#D3D3D3", f"price\n")]
        counts = [("#D3D3D3", f"count\n")]
        
        nr = 0
        combined_width = 0
        for result in sorted(response.search_result, key= lambda x: x.category):
            nr += 1
            
            nrs.append( ("#D3D3D3", f"{nr}\n") )
            names.append( ("#00BFFF", f"{result.name}\n") )
            prices.append( ("#D3D3D3", f"$ {str(result.price)}\n") )
            counts.append( ("#D3D3D3", f"{str(result.count)}\n") )
        
        info = [ nrs, names, prices, counts ]
        formatted = map(lambda x: FormattedText(x), info)
        ftc = map(lambda x: FormattedTextControl(x), formatted)
        wins = map(lambda x: Window(x,dont_extend_width=True), ftc)
        body = VSplit( wins, align=HorizontalAlign.LEFT, padding=2 )
        body.width = body.preferred_width( os.get_terminal_size().columns ).preferred
        inner_box = Box(body, padding_left=1, padding_right=1)
        frame = Frame(inner_box)
        box = Box(frame, padding_left=1)
        
        print_container(box)