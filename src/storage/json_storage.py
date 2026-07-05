import json
from pathlib import Path

from models.product import Product

DATA_FILE = Path("data/products.json")


def load_products():
    if not DATA_FILE.exists():
        return[] 
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Product.from_dict(item) for item in data]

def save_products(products):
    data = [product.to_dict() for product in products]

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)