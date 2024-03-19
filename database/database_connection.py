
import mysql.connector


class DatabaseConnection(object):
    
    # Singleton --------------------------------
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    # ------------------------------------------

    def __init__(self) -> None:
        self.setup_database_connection()
    
    _db: mysql.connector.MySQLConnection
    _db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Kom12345",
            "database": "warehouse"
    }
    
    def setup_database_connection(self):
        #self._db_config = db_config
        self._db = self._connect_mysql()

    
    # def setup_database_connection(self, db_config: dict):
    #     self._db_config = db_config
    #     self._db = self._connect_mysql()
        
    
    def _connect_mysql(self) -> mysql.connector.MySQLConnection:
        self._db = mysql.connector.connect(
            host = self._db_config["host"],
            user = self._db_config["user"],
            password = self._db_config["password"],
            database = self._db_config["database"]
        )
        return self._db
    
    def query_database(self, query: str) -> dict:
        cursor = self._db.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    # def query_database_procedure(self, query: str) -> dict:
    #     cursor = self._db.cursor(dictionary=True)
    #     cursor.callproc("SearchByName")
    #     return cursor.fetchall()