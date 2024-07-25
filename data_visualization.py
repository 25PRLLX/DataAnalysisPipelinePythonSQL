import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

def visualize_data(csv_path='product_sales.csv'):
    product_sales = pd.read_csv(csv_path, index_col='product')

    product_sales.plot(kind='bar')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.savefig('sales_by_product.png')
    plt.show()

    logging.info("Data visualization completed successfully.")

if __name__ == "__main__":
    visualize_data()


