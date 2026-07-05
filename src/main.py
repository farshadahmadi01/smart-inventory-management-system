
from models.product import Product 
from storage.json_storage import load_products, save_products
from services.product_service import ProductService

service = ProductService()

def show_menu():
    print("\n=== Smart Inventory & Sales Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product by Barcode")
    print("4. Exit")

def add_product():
    name = input("Product name: ")
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    service.add_product(name, barcode, price, quantity)

    print("\nProduct added successfully!")

def view_products():
    products = service.get_all_products()

    if not products:
        print("\nNo products found.")
        return
        
    for product in products:
        product.display()

def search_products():
    barcode = input("Enter Barcode: ")
    
    product = service.find_by_barcode(barcode)

    if product:
        product.display()
    else:
        print("Product not found.")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "4":
            print("Goodbye!")
            break

        elif choice == "3":
            search_products()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__": 
    main()