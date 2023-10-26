import csv


class Item:    
    payRate = 0.8

    all = list()

    def __init__(self, name:str, price:float, quantity=0) -> None:
        self.name     = name
        self.price    = price
        self.quantity = quantity

        assert self.price >= 0, f"Price {self.price} is not greater or equal than zero"
        assert self.quantity >= 0, f"Quantity {self.quantity} is not greater or equal than zero"

        Item.all.append(self)

    def __repr__(self) -> str:
        return f'repr: Item({self.name}, {self.price}, {self.quantity})'

    def calculate_price(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self) -> float:
        return self.calculate_price * self.payRate
    
    @classmethod
    def instantiate_from_csv(cls) -> None:
        with open('items.csv', 'r') as file:
            content = csv.DictReader(file)
            items = list(content)

        for item in items:
            Item(
                name     = item.get('name'),
                quantity =int(item.get('quantity')),
                price    =int(item.get('price'))
            ) 

# item1 = Item("bola", 15, 5)
# item2 = Item("Celular", 1500, 1)

# print(f"{Item.__dict__}\n")
# print(f"{item1.__dict__}\n")

Item.instantiate_from_csv()

for item in Item.all:
    print(item.name)
    print(f'{item}\n')