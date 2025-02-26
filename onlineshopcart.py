# Sultan Nurfalah
# TI23H
class CartItem:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    
    def add_item(self, quantity):
        self.quantity += quantity
        print(f"Added {quantity} more of '{self.item_name}'. Total: {self.quantity}")
    
    def remove_item(self, quantity):
        if quantity >= self.quantity:
            print(f"Removed '{self.item_name}' from the cart.")
            self.quantity = 0
        else:
            self.quantity -= quantity
            print(f"Removed {quantity} of '{self.item_name}'. Remaining: {self.quantity}")
    
    def calculate_total(self):
        return self.price * self.quantity


item1 = CartItem("Laptop", 10000000, 1)
item1.add_item(2)
item1.remove_item(1)
print(f"Total price: Rp{item1.calculate_total()}")
item1.remove_item(2)
print(f"Total price after removal: Rp{item1.calculate_total()}")
