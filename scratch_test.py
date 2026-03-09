from models import Customer, Transaction, FoodItem, Menu

burger = FoodItem("Spicy Burger", 8.99, "Entree", 4.7)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
cake = FoodItem("Chocolate Cake", 5.25, "Desserts", 4.8)

menu = Menu([burger, soda, cake])

transaction = Transaction([burger, soda])

customer = Customer("Kery", [transaction])

print(customer.name)
print(transaction.compute_total())
print(menu.filter_by_category("Drinks")[0].name)