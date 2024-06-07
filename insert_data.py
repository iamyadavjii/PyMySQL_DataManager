from connect_db import create_connection

def insert_family_data(connection, name, last_name, age, occupation, location, relation):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO family_details (name, last_name, age, occupation, location, relation) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (name, last_name, age, occupation, location, relation)
    cursor.execute(insert_query, data)
    connection.commit()
