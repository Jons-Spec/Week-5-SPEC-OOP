from src.logger import logger
from src.shirts import TShirt
from src.pants import Pants


class ClothesFactory:
    @staticmethod
    def create_clothes(clothes_type, size, color, connection,database_name,**kwargs):
        if clothes_type == "tshirt":
            clothes = TShirt(size, color, kwargs.get('design', ''))
        elif clothes_type == "pants":
            clothes = Pants(size, color, kwargs.get('style', ''))
        else:
            raise ValueError("Invalid clothes type")

        # Store clothes in the database
        cursor = connection.cursor()
    
        try:
            # Create the clothes table if it doesn't exist
            ClothesFactory.create_clothes_table(cursor, database_name)

            cursor.execute(f'USE {database_name}')
            cursor.execute('INSERT INTO clothes (type, size, color, design, style) VALUES (%s, %s, %s, %s, %s)',
                           (clothes_type, size, color, kwargs.get('design', ''), kwargs.get('style', '')))
            connection.commit()

            # Retrieve the last inserted ID
            cursor.execute("SELECT LAST_INSERT_ID()")
            last_inserted_id = cursor.fetchone()[0]

            # Add the ID to the clothes object
            clothes.id = last_inserted_id

            logger.info(f"{clothes_type.capitalize()} added to the database with ID {last_inserted_id}.")
        except Exception as e:
            logger.error(f"Error occurred while adding {clothes_type}: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()

        return clothes
    
    @staticmethod
    def create_clothes_table(cursor, database_name):
        try:
            cursor.execute(f'USE {database_name}')
            cursor.execute('''CREATE TABLE IF NOT EXISTS clothes (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                type VARCHAR(50) NOT NULL,
                                size VARCHAR(50) NOT NULL,
                                color VARCHAR(50) NOT NULL,
                                design VARCHAR(50),
                                style VARCHAR(50)
                            )''')
            logger.info("Table 'clothes' created successfully.")
        except Exception as e:
            logger.error(f"Error occurred while creating 'clothes' table: {e}")
