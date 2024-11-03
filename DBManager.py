import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quiz (
            id INT PRIMARY KEY,
            title VARCHAR (255),
            description TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Questions (
            id INT PRIMARY KEY,
            quiz_id INT,
            content TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Options (
            id INT PRIMARY KEY,
            content TEXT,
            is_correct BOOLEAN);
        """)
        self.connection.commit()