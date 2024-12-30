import mysql.connector

def query(query_string: str):
    connection = mysql.connector.connect(
        user="local_user",
        password="local_password",
        database="taskmaster",
    )
    
    cursor = connection.cursor()
    cursor.execute(query_string)
    
    results = cursor.fetchall()
    connection.close()
    
    return results

