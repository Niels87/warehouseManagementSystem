from database import database_connection, database_interaction, database_builder

"""A wrapper class around the
    DatabaseConnection (handles the connection),
    DatabaseBuilder (sets up the database incl. stored procedures),
    and DatabaseInteraction (calls stored procedures) classes."""
class DatabaseHandler(object):
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------

    def __init__(self, config: dict) -> None:
        self._config = config
        self._db_connection = database_connection.DatabaseConnection(config)
        self._db_interaction = database_interaction.DatabaseInteraction(self.db_connection)
        self._db_builder = database_builder.DatabaseBuilder(self.db_connection, config)
    
    @property
    def config(self):
        return self._config

    @property
    def db_connection(self):
        return self._db_connection

    @property
    def db_interaction(self):
        return self._db_interaction

    @property
    def db_builder(self):
        return self._db_builder

    # create_database() must be run befor set_database().
    # cannot connect to a database, that doesn't exist.
    def create_and_set_database(self):
        self.db_builder.create_database() 
        self.db_connection.set_database()
        
    def drop_database(self):
        self.db_builder.drop_database()    
    
    def initialize_database(self):
        self.db_builder.create_tables()
        self.db_builder.create_procedures()