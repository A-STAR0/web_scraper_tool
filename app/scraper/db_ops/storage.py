import json
import os
from ..schemas import Product


class Storage:
    def __init__(self, filename=os.getenv('DB_FILE', 'scraped_data.json')):
        self.filename = filename
        self.data = self.load_data()
        self.cache = self.initialize_cache()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        # Serialize to JSON file
        with open(self.filename, 'w') as scraped_data:
            json.dump(self.data, scraped_data, default=lambda x: x.__dict__, indent=2)

    def initialize_cache(self):
        cache = {}
        for product in self.data:
            cache[product['product_title']] = product['product_price']
        return cache

    def should_update(self, product_data: Product):
        title = product_data.product_title
        price = product_data.product_price
        if title in self.cache:
            if self.cache[title] != price:
                self.cache[title] = price
                return True
            return False
        else:
            self.cache[title] = price
            return True

    def add_or_update_product(self, product_data: Product):
        title = product_data.product_title
        updated = False
        for product in self.data:
            if product['product_title'] == title:
                if product['product_price'] != product_data.product_price:
                    product['product_price'] = product_data.product_price
                    updated = True
                break
        if not updated:
            self.data.append(product_data.__dict__)
