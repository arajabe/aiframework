import mysql.connector

def get_db_connection():
    mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Nannilam@123",  # Change this
        database="testdb")

def save_message(session_id:str, sender:str, message:str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO conversations (session_id, sender, message) VALUES (%s, %s, %s)",
        (session_id, sender, message))
    connection.commit()
    cursor.close()
    connection.close()

def load_history(session_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sender, message FROM conversations WHERE session_id=%s ORDER BY id ASC",
        (session_id,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows