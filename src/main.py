from models.product import Product

products = []

def show_menu():
    print("\n=== Smart Inventory & Sales Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

def add_product():
    print("\nAdd New Product")

    name = input("Product name: ")
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = Product(name, barcode, price, quantity)
    products.append(product)
    print("\nProduct added successfully!")

def view_products():
    if not products:
        print("\nNo products found.")
        return
        
    print("\nProduct List")

    for product in products:
        product.display()


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()