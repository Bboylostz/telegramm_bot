import sqlite3
from typing import List, Tuple
from config import db_connection
class Database:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                image_path TEXT,
                ingredients TEXT,
                instructions TEXT
            )
        ''')
        self.conn.commit()

    def add_recipe(self, name: str, type_: str, image_path: str, ingredients: List[str], instructions: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO recipes (name, type, image_path, ingredients, instructions)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, type_, image_path, ', '.join(ingredients), instructions))
        self.conn.commit()

    def get_random_recipe(self, type_: str) -> Tuple:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM recipes WHERE type = ? ORDER BY RANDOM() LIMIT 1', (type_,))
        return cursor.fetchone()

    def close(self):
        self.conn.close()
