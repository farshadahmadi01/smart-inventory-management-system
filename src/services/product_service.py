from storage.json_storage import load_products, save_products
from models.product import Product

class ProductService:
    def __init__(self):
        self.products = load_products()

    def add_product(self, name, barcode, price, quantity):
        product = Product(name, barcode, price, quantity)

        self.products.append(product)

        save_products(self.products)

    def get_all_products(self):
        return self.products
    
    def find_by_barcode(self, barcode):
        for product in self.products:
            if product.barcode == barcode:
                return product
            
        return None