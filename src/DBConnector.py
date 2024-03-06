from typing import Dict
import mysql.connector as mysql

class DBConnection:
    
    __instance = None

    def __init__(self,host: str, username:str, password: str, port:str, database: str=None) -> None:
        self.host = host
        self.user = username
        self.password = password
        self.port = port
        self.database = database

        
        if DBConnection.__instance is None:
            DBConnection.__instance = mysql.connect(host=self.host, username=self.user, password=self.password, port=self.port)
            if self.database:
                self.create_database(self.database)
        else:
            raise Exception("Can't creat another MySQL connection")
        
    def create_database(self, database_name: str) -> None:
        cursor = DBConnection.__instance,cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
        cursor.close()

        
    @staticmethod
    def get_instance(credantials: Dict[str,str]) -> object:
        if not DBConnection.__instance:
            DBConnection(credantials['DB_HOST'], credantials['DB_USER'], credantials['DB_PASS'],credantials['DB_PORT'])
        return DBConnection.__instance
    
    @staticmethod
    def close_instance() -> None:
        DBConnection.__instance.close()