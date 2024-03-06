from typing import Dict
import mysql.connector as mysql

class DBConnection:
    
    __instance = None

    def __init__(self,host: str, username:str, password: str, port:str) -> None:
        self.host = host
        self.user = username
        self.password = password
        self.port = port
        
        if DBConnection.__instance is None:
            DBConnection.__instance = mysql.connect(host=self.host, username=self.user, password=self.password, port=self.port)
        else:
            raise Exception("Can't creat another MySQL connection")
        
    @staticmethod
    def get_instance(credantials: Dict[str,str]) -> object:
        if not DBConnection.__instance:
            DBConnection(credantials['DB_HOST'], credantials['DB_USER'], credantials['DB_PASS'], credantials['DB_PORT'])
        return DBConnection.__instance
    
    @staticmethod
    def close_instance() -> None:
        DBConnection.__instance.close()