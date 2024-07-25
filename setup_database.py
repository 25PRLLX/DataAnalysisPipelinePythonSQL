import sqlite3
from contextlib import closing
import logging

logging.basicConfig(level=logging.INFO)

def setup_database(db_path='example.db'):
    with closing(sqlite3.connect(db_path)) as conn, conn, closing(conn.cursor()) as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                product TEXT,
                quantity INTEGER,
                price REAL
            )
        ''')

        sales_data = [
            ('2024-01-01', 'Product A', 10, 9.99),
            ('2024-01-02', 'Product B', 5, 19.99),
            ('2024-01-03', 'Product A', 7, 9.99),
            ('2024-01-04', 'Product C', 3, 29.99),
            ('2024-01-05', 'Product B', 2, 19.99)
        ]

        cursor.executemany('''
            INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?)
        ''', sales_data)

        conn.commit()
        logging.info("Database setup complete successfully.")

if __name__ == "__main__":
    setup_database()
