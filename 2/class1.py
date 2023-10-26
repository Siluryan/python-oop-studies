class Item:
    
    payRate = 0.8

    def __init__(self, name:str, price:float, quantity=0) -> None:
        self.name     = name
        self.price    = price
        self.quantity = quantity

        assert self.price >= 0, f"Price {self.price} is not greater or equal than zero"
        assert self.quantity >= 0, f"Quantity {self.quantity} is not greater or equal than zero"

    def calculate_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.calculate_price * self.payRate

item1 = Item("bola", 15, 5)
item2 = Item("Celular", 1500, 1)

print(f"{Item.__dict__}\n")
print(f"{item1.__dict__}\n")