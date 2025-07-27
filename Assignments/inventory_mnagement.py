inventory = {
    "apples": {"price": 1.20, "quantity": 100},
    "bananas": {"price": 1.20, "quantity": 50},
    "oranges": {"price": 1.20, "quantity": 85},
}

# Q1] Add a new product to the inventory with its price and quantity.

inventory["Guavas"] = {"price": 1.50, "quantity": 12}

# Q2] Update the price of an existing product (e.g., change the price of "bananas").

inventory["bananas"]["price"] = 1.30

# Q3] Simulate the sale of 25 apples by updating the quantity accordingly.
inventory["apples"]["quantity"] -= 25

# Q4] Identify and print all products whose quantity is below 100.

low_stock_products = {product: details for product, details in inventory.items() if details["quantity"] < 100}

