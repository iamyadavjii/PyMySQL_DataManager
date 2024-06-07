from connect_db import create_connection

def create_family_details_table(connection):
    cursor = connection.cursor()
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS family_details (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255),
        age INT,
        occupation VARCHAR(255),
        location VARCHAR(255),
        relation VARCHAR(255)
    )
    """
    cursor.execute(table_creation_query)
    connection.commit()
