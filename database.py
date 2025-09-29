from model import item
from typing import List
import sqlite3

class itemDAO:
    def __init__(self):
        self.DB_NAME = 'itens.db'
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        );
        """)
        conn.commit()
        conn.close()
    def get_db_connection(self):
        conn = sqlite3.connect(self.DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    def add_item(self, item: item):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
            (item.get_descricao(), item.get_quantidade())
        )
        conn.commit()
        conn.close()

    def fetch_all_itens(self) -> List[item]:
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens")
        rows = cursor.fetchall()
        conn.close()
        return [
            item(row['id'],row['descricao'],row['quantidade']) for row in rows
        ]
