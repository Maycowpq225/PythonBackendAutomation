import mysql.connector
import os
from dotenv import load_dotenv

class DBConnection:
    def __init__(self):
        load_dotenv(os.path.join('env', "db.env"))

        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )

    def cursor(self):
        return self.conn.cursor(dictionary=True)