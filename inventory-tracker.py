#Store inventory and stock tracker


class Product:

  def __init__(self, product_id, name, price, stock):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.stock = stock

  def sell(self, quantity):
    if quantity <= 0:
      print("Invalid quantity.")
    elif quantity <= self.stock:
      self.stock -= quantity
      total = quantity * self.price
      print(f"Sold {quantity} x {self.name} | Total: rs. {total}")
    else:
      print(f"Out of stock: Only {self.stock} units of {self.name} left.")

  def restock(self, quantity):
    if quantity > 0:
      self.stock += quantity
      print(f"Restocked {self.name}: {self.stock} units available.")

  def display_info(self):
    print(
        f"[{self.product_id}] {self.name} | Price: rs. {self.price} | Stock:"
        f" {self.stock}"
    )


#Sample product operations....
item_1 = Product("P191", "Wireless mouse", 8980, 12)
item_2 = Product("P132", "Mechanical keyboard", 6750, 5)
item_3 = Product("P067", "USB-C cable", 3720, 17)

print("Initial Inventory....")
item_1.display_info()
item_2.display_info()
item_3.display_info()

print("\nDaily Transactions.....")
item_1.sell(3)
item_2.sell(6)  # low-stock check
item_2.restock(5)
item_2.sell(6)

print("\nUpdated inventory....")
item_1.display_info()
item_2.display_info()
item_3.display_info()
