def offer(product):
    offers = {
        "Laptop": "10% off",
        "Phone": "5% cashback",
        "Tablet": "Free case",
        "Monitor": "20% off"
    }
    return offers.get(product, "No offer available.")