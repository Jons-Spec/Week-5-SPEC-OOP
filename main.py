from src.db_connector import DBConnection
from src.logger import logger
from src.clothes_factory import ClothesFactory
from src.credentials import credentials



VALID_COLORS = ["red", "blue", "green", "yellow", "black", "white"]
VALID_TSHIRT_DESIGNS = ["stripes", "polka dots", "solid", "graphic"]
VALID_PANTS_STYLES = ["jeans", "khakis", "chinos", "cargo"]

def main():
    connection = DBConnection.get_instance(credentials)
    if connection:
        logger.info("Successfully connected to the database.")
    else:
        logger.error("Failed to connect to the database.")
        return None
        
    database_name = credentials['DB_NAME']
    created = DBConnection.create_database(connection, database_name)
    if created:
        logger.info(f"Database '{database_name}' created successfully.")
    else:
        logger.info(f"Database '{database_name}' already exists.")
    
    while True:
        try:
            clothes_type = input("Enter the type of clothes (tshirt/pants): ").lower()
            if clothes_type not in ["tshirt", "pants"]:
                logger.error("Invalid clothes type. Please enter 'tshirt' or 'pants'.")
                continue

            size_input = input("Enter the size (S/M/L/XL): ").upper()
            size_mapping = {"S": "Small", "M": "Medium", "L": "Large", "XL": "Extra Large"}
            size = size_mapping[size_input]
            print(size)

            color = input(f"Enter the color ({', '.join(VALID_COLORS)}): ").lower()
            if color not in VALID_COLORS:
                logger.error(f"Invalid color. Please choose from: {', '.join(VALID_COLORS)}")
                continue

            if clothes_type == "tshirt":
                design = input(f"Enter the design ({', '.join(VALID_TSHIRT_DESIGNS)}): ").lower()
                if design not in VALID_TSHIRT_DESIGNS:
                    logger.error(f"Invalid design. Please choose from: {', '.join(VALID_TSHIRT_DESIGNS)}")
                    continue
                style = ""
            else:
                style = input(f"Enter the style ({', '.join(VALID_PANTS_STYLES)}): ").lower()
                if style not in VALID_PANTS_STYLES:
                    logger.error(f"Invalid style. Please choose from: {', '.join(VALID_PANTS_STYLES)}")
                    continue
                design = ""

            clothes = ClothesFactory.create_clothes(clothes_type, size, color, design=design,connection=connection,database_name=database_name, style=style,)
            logger.info(f"{clothes} created successfully!")

        except KeyError:
            logger.error("Invalid size. Please enter 'S', 'M', 'L', or 'XL'.")

        except ValueError as e:
            logger.error(f"Error: {e}")

        choice = input("Do you want to create another clothes? (yes/no): ")
        if choice.lower() != "yes":
            break


if __name__ == "__main__":
    main()
