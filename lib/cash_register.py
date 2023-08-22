class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.append((title, price, quantity))

    def void_last_transaction(self):
        if self.items:
            title, price, quantity = self.items.pop()
            self.total -= price * quantity
    
    def apply_discount(self):
        self.total -= (self.total * self.discount / 100)
    
    def itemize_receipt(self):
        itemized = []
        for title, price, quantity in self.items:
            if quantity > 1:
                itemized.append(f"{title} ({quantity}) - ${price * quantity:.2f}")
            else:
                itemized.append(f"{title} - ${price:.2f}")
        return "\n".join(itemized)

# Run some test cases
register = CashRegister(10)  # Create a CashRegister instance with a 10% discount
register.add_item("Apple", 0.5)
register.add_item("Banana", 0.3, 3)
print("Items in cart:")
print(register.itemize_receipt())
print(f"Total before discount: ${register.total:.2f}")

register.apply_discount()
print(f"Total after discount: ${register.total:.2f}")

register.void_last_transaction()
print("After voiding last transaction:")
print(register.itemize_receipt())
print(f"Total after voiding: ${register.total:.2f}")
