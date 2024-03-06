from src.credentials import (HOST, USERNAME,PASSWORD,DATABASE,PORT)
from src.DBConnector import DBConnection
from src.logger import logger
import time

def main() -> None:
    try:
        credentials = {
            "DB_HOST" : HOST,
            "DB_USER" : USERNAME,
            "DB_PASS" : PASSWORD,
            "DB_NAME" : DATABASE,
            "DB_PORT" : PORT,
        }
        connection = DBConnection.get_instance(credentials)
        logger.info(f'Connected sucessfully to MySQL database: {connection}')
        database_name = credentials['DB_NAME']
        # Call create_database method on the DBConnection instance
        database = DBConnection.create_database(connection, database_name)  # Pass the DBConnection instance as the first argument
        if database == None:
            logger.info(f'Database already exists did not create a new one: {database}')
        else:
            logger.info(f'Database created: {database}')
        time.sleep(10)
        DBConnection.close_instance()
        logger.info(f'MySQL database closed successfully: {connection}')

    except TypeError as error:
        logger.error(f'Error connecting to MySQL database: {error}')  
        DBConnection.close_instance()  


if __name__ == "__main__":
    main()