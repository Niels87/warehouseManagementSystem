
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
        self._db = self._connect_mysql()

    @property
    def db(self):
        return self._db
    
    _db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Kom12345",
    }  
    
    def _connect_mysql(self) -> mysql.connector.MySQLConnection:
        self._db = mysql.connector.connect(
            host = self._db_config["host"],
            user = self._db_config["user"],
            password = self._db_config["password"]
        )
        return self._db
    
    def set_database(self, db_name: str):
        self.db.database = db_name
        
    def query_database(self, query: str) -> dict:
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        if cursor.with_rows == True:
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
        self.db.commit()
        cursor.close()
        return result
    
    def call_stored_procedure(self, proc_name: str, proc_args: tuple) -> dict:
        with self.db.cursor(dictionary=True) as cursor:
            cursor.callproc(proc_name, proc_args)
            for r in cursor.stored_results():
                result = r.fetchall()
        self.db.commit()
        try:
            return result
        except:
            return
        