from sales_data import PRODUCTS

def get_price(product):
    return PRODUCTS.get(product, "Product not found.")