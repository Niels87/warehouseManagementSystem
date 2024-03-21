from events import search_database, add_item, remove_item, update_item
import asyncio

class CommandLineInterface(object):
    
    
    def __init__(self) -> None:
        self._choices = {
            "1": self.search,
            "2": self.add_item,
            "3": self.remove_item,
            "4": self.update_item
            }
    
    def print_start_menu(self):
        print("\nWelcome. What do you want to do?")
        line = "----------------------------------------"
        print("\n" + line)
        width = line.__len__()-1
        ws = "{" + f":<{width}"+ "}"
        
        for key in self._choices:
            option = self._choices[key].__name__.replace("_", " ").capitalize()
            s = f"| ({key}) - {option}"
            fs = ws.format(s) + "|"
            print(fs)
            
        cancel = ws.format("| (0) - Cancel") + "|"
        print(cancel)
        print(line + "\n")
        
    
    def start_menu(self):
        
        self.print_start_menu()
        choice = input("-> ")
        
        if choice in self._choices:
            self._choices[choice]()
        elif choice == '0':
            print("See you later!")
            return
        else:
            print("Choice not recognised, please chose one of the available options.")
            self.start_menu()
                
    def search(self):
        print("\nSearch:")
        search_str = input("-> ")
        search_database.SearchDatabaseRequest(search_str).post()
        self.start_menu()
        
    
    def add_item():
        pass
    
    def remove_item():
        pass
    
    def update_item():
        pass
    
    
    

