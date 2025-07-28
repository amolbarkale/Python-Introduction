from collections import defaultdict

class Product:
    total_products = 0
    category_counter = defaultdict(int)

    def __init__(self, product_id, name, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

        Product.total_products += 1
        Product.category_counter[category] += 1

    def get_product_info(self):
        return f"{self.name} (${self.price}) - {self.category}"

    def place_order(self, quantity=1):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        return False

    @classmethod
    def get_total_products(cls):
        return cls.total_products

    @classmethod
    def get_most_popular_category(cls):
        return max(cls.category_counter, key=cls.category_counter.get)


class Customer:
    total_revenue = 0

    def __init__(self, customer_id, name, email, membership="regular"):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.membership = membership

    def get_discount_rate(self):
        return {"regular": 0, "premium": 10, "gold": 20}.get(self.membership.lower(), 0)

    def __str__(self):
        return f"{self.name} ({self.membership.title()})"

    @classmethod
    def add_revenue(cls, amount):
        cls.total_revenue += amount

    @classmethod
    def get_total_revenue(cls):
        return round(cls.total_revenue, 2)


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = defaultdict(int)  # product_id: quantity
        self.products = {}  # product_id: Product

    def add_item(self, product, quantity=1):
        self.items[product.product_id] += quantity
        self.products[product.product_id] = product

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            del self.products[product_id]

    def clear_cart(self):
        self.items.clear()
        self.products.clear()

    def get_total_items(self):
        return sum(self.items.values())

    def get_cart_items(self):
        return {self.products[pid].name: qty for pid, qty in self.items.items()}

    def get_subtotal(self):
        subtotal = sum(self.products[pid].price * qty for pid, qty in self.items.items())
        return round(subtotal, 2)

    def calculate_total(self):
        subtotal = self.get_subtotal()
        discount_rate = self.customer.get_discount_rate()
        final = subtotal * (1 - discount_rate / 100)
        Customer.add_revenue(final)
        return round(final, 2)

    def place_order(self):
        success = True
        for pid, qty in self.items.items():
            if not self.products[pid].place_order(qty):
                success = False
        return success
