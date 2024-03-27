from ui.cli.cli import CommandLineInterface
from event_system.event_handler import EventHandler
from database.database_handler import DatabaseHandler
from ui.printing.request_printer import RequestPrinter
from ui.printing.response_printer import ResponsePrinter
from database.simulator import Simulator


"""
The wrapper around the whole application.
Contains 4 main parts: 
A CommandLineInterface (CLI), handles user input.
A DatabaseHandler, handles everything database related,
An EventHandler, handles requests and responses 
between the CLI and the database.
And a Simulator class used to send request to the database, 
in order to simulate a history of use.
"""
class WarehouseApp(object):
    
    def __init__(self, config: dict, debug_mode=False ) -> None:
        self._debug_mode: bool = debug_mode
        self._event_handler = EventHandler()
        self._cli = CommandLineInterface()
        self._db_handler = DatabaseHandler(config)
        self.setup()
    


    def run(self):
        self._cli.start()

    def setup(self):
        
        self._db_handler.drop_database()
        self._db_handler.create_database()
        print("- Database created")
        self._db_handler.initialize_database()
        print("- Tables and procedures created")
        
        self.simulate_inputs()
        print("- Items added")
        
        self._request_printer = RequestPrinter()
        self._response_printer = ResponsePrinter()
        self.setup_debugmode()
        
    def setup_debugmode(self):
        if self._debug_mode == False:
            return
        self._event_handler.debug_mode = True
    
        
    def dismantle_session(self):
        self._db_handler.drop_database()
        print("\nDatabase dropped")
        print("Goodbye!")

    def simulate_inputs(self):
        sim = Simulator()
        sim.run()
        
    