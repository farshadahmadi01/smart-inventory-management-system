def show_menu():
    print("\n=== Smart Inventory & Sales Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add Product feature coming soon...")
        elif choice == "2":
            print("View Products feature coming soon...")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()