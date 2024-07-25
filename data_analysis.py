import pandas as pd
import logging
from database import Database

logging.basicConfig(level=logging.INFO)

def analyze_data(db_path='example.db'):
    db = Database(db_path)
    rows = db.query('SELECT * FROM sales')

    df = pd.DataFrame(rows, columns=['id', 'date', 'product', 'quantity', 'price'])

    df['total_sales'] = df['quantity'] * df['price']
    product_sales = df.groupby('product')['total_sales'].sum()

    logging.info("Data analysis completed successfully.")
    logging.info(product_sales)

    product_sales.to_csv('product_sales.csv')

if __name__ == "__main__":
    analyze_data()