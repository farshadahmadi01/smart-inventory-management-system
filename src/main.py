
from models.product import Product 
from storage.json_storage import load_products, save_products

products = load_products()

def show_menu():
    print("\n=== Smart Inventory & Sales Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product by Barcode")
    print("4. Exit")

def add_product():
    print("\nAdd New Product")

    name = input("Product name: ")
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = Product(name, barcode, price, quantity)
    products.append(product)
    save_products(products)
    print("\nProduct added successfully!")

def view_products():
    if not products:
        print("\nNo products found.")
        return
        
    print("\nProduct List")

    for product in products:
        product.display()

def search_products():
    barcode = input("Enter Barcode: ")
    
    for product in products:
        if product.barcode == barcode:
            print("\nProduct found")
            product.display()
            return
        
    print("\nProduct not found.")

    

            


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