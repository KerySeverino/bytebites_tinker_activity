from models import Customer, FoodItem, Transaction, Menu

burger = FoodItem("Spicy Burger", 8.99, "Entree", 4.7)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
cake = FoodItem("Chocolate Cake", 5.25, "Desserts", 4.9)
juice = FoodItem("Orange Juice", 3.75, "Drinks", 4.5)

menu = Menu([burger, soda, cake, juice])

transaction = Transaction([burger, soda, juice])
customer = Customer("Kery", [transaction])

print("Customer:", customer.name)

print("\nDrinks:")
for item in menu.filter_by_category("Drinks"):
    print(item.name)

print("\nSorted by popularity:")
for item in menu.sort_by_popularity():
    print(item.name, item.popularity_rating)

print("\nTransaction total:")
print(transaction.compute_total())