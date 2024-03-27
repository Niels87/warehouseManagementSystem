from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from items.items import WarehouseItem
from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Frame, Box
from prompt_toolkit.layout.containers import VSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from builtins import map
from prompt_toolkit.layout import HorizontalAlign
from utils.color_palette import Colors
import os


"""
Formats and prints items. Either single item or multiple
items as a table. The function for table printing is quite
messy. Have not yet found an elegant way to simplify it.
"""
class ItemPrinter(object):
    
    
    @staticmethod
    def print_item(item: WarehouseItem):
        pass
        
    
    @staticmethod
    def print_table_of_items(items: list[WarehouseItem]):
        print("")
        
        nrs = [(Colors.LightGrey, f" \n\n")]
        names = [(Colors.LightGrey, f"name\n\n")]
        prices = [(Colors.LightGrey, f"price $\n\n")]
        counts = [(Colors.LightGrey, f"count\n\n")]
        categories = [(Colors.LightGrey, f"category\n\n")] 
        ids = [(Colors.Grey, f"id\n\n")] 
        
        nr = 0
        for result in sorted(items, key= lambda x: x.category):
            nr += 1
            
            nrs.append( (Colors.LightGrey, f"{nr}\n") )
            names.append( (Colors.LightBlue, f"{result.name}\n") )
            prices.append( (Colors.MutedGreen, f"{str(result.price)}\n") )
            counts.append( (Colors.MutedYellow, f"{str(result.count)}\n") )
            categories.append( (Colors.LightGrey, f"{str(result.category)}\n") )
            ids.append( (Colors.Grey, f"{result.id}\n") )
            
        
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