class Product:
    def __init__(self, name, barcode, price, quantity):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.quantity = quantity

    def display(self): 
        print("\nProduct Information")
        print("---------------------")
        print(f"Name        : {self.name}")
        print(f"Barcode     : {self.barcode}")
        print(f"Price       : ${self.price:.2f}")
        print(f"Quantity    : {self.quantity}")

    def to_dict(self):
        return{
            "name": self.name,
            "barcode": self.barcode,
            "price": self.price,
            "quantity": self.quantity,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["barcode"],
            data["price"],
            data["quantity"],
        )