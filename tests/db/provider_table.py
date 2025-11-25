from utils.db_connection import DBConnection

def get_provider_by_email(email):
    query = "SELECT * FROM provider WHERE email = %s"

    db = DBConnection()
    cursor = db.cursor()

    cursor.execute(query, (email,))
    data = cursor.fetchone()

    cursor.close()
    return data