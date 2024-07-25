import sqlite3
from contextlib import closing
import logging

logging.basicConfig(level=logging.INFO)

class Database:
    def __init__(self, db_path='example.db'):
        self.db_path = db_path

    def query(self, sql, params=None):
        with closing(sqlite3.connect(self.db_path)) as conn, conn, closing(conn.cursor()) as cursor:
            cursor.execute(sql, params or [])
            rows = cursor.fetchall()
            return rows
        
if __name__ == "__main__":
    db = Database()
    results = db.query('SELECT * FROM sales')
    for row in results:
        logging.info(row)