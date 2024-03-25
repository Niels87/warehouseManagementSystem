from ui.cli.cli import CommandLineInterface
from event_handler import EventHandler
from database.database_handler import DatabaseHandler
from ui.request_printer import RequestPrinter
from ui.response_printer import ResponsePrinter
from simulator import Simulator

class WarehouseApp(object):
    
    def __init__(self, config: dict) -> None:
        self._cli = CommandLineInterface()
        self._event_handler = EventHandler()
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
        
    def dismantle_session(self):
        self._db_handler.drop_database()
        print("\nDatabase dropped")
        print("Goodbye!")

    def simulate_inputs(self):
        sim = Simulator()
        sim.run()