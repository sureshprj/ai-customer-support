import matplotlib.pyplot as plt
from sales_data import SALES_HISTORY

def generate_sales_chart(product):
    months = SALES_HISTORY["labels"]
    sales = SALES_HISTORY.get(product)
    if not sales:
        return None

    plt.figure()
    plt.plot(months, sales, marker='o')
    plt.title(f"Sales Trend - {product}")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    chart_path = f"{product.lower()}_sales_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path