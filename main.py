from src.credentials import (HOST, USERNAME,PASSWORD,DATABASE,PORT)
from src.DBConnector import DBConnection
from src.logger import logger

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
        database = DBConnection.create_database(DATABASE)
        logger.info(f'Database created {database}')

    except TypeError as error:
        logger.error(f'Error connecting to MySQL database: {error}')    


if __name__ == "__main__":
    main()