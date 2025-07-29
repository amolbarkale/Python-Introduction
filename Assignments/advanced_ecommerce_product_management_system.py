import re

class Product:
    VALID_CATEGORIES = ["Electronics", "Clothing", "Books", "Home", "Sports"]

    def __init__(self, name, base_price, discount_percent, stock_quantity, category):
        self.name = name
        self.base_price = base_price
        self.discount_percent = discount_percent
        self.stock_quantity = stock_quantity
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (3 <= len(value) <=50):
            raise ValueError("Name must be 3-50 characters")
        if not re.match(r'^[a-zA-Z0-9\s]+$', value):
            raise ValueError("Name can only contain alphanumeric characters and spaces")
        self._name = value

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value <= 0 or value > 50000:
            raise ValueError("Base price must be between 0 and 50000")
        self._base_price = value

    @property
    def discount_percent(self):
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Discount percent must be between 0 and 100")
        self._discount_percent = round(value,2)

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if not isinstance(value, int) or value < 0 or value > 10000:
            raise ValueError("Stock must be a non-negative integer (≤ 10,000)")
        self._stock_quantity = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in Product.VALID_CATEGORIES:
            raise ValueError(f"Category must be one of: {Product.VALID_CATEGORIES}")
        self._category = value

    @property
    def final_price(self):
        return round(self.base_price * (1 - self.discount_percent / 100), 2)

    @property
    def savings_amount(self):
        return round(self.base_price - self.final_price, 2)

    @property
    def availability_status(self):
        if self.stock_quantity == 0:
            return "Out of Stock"
        elif self.stock_quantity < 10:
            return "Low Stock"
        else:
            return "In Stock"

    @property
    def product_summary(self):
        return (
            f"{self.name} | ${self.base_price:.2f} | {self.discount_percent:.2f}% off | "
            f"Final: ${self.final_price:.2f} | Status: {self.availability_status}"
        )