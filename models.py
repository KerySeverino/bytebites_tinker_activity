# ByteBites backend model scaffolds
# Classes:
# - Customer: stores a customer's name and purchase history
# - Transaction: stores selected food items and can compute total cost
# - FoodItem: stores information about a menu item
# - Menu: stores all food items and can filter by category


class Customer:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def compute_total(self):
        total = 0
        for item in self.selected_items:
            total += item.price
        return total


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter_by_category(self, category):
        filtered_items = []

        for item in self.items:
            if item.category == category:
                filtered_items.append(item)

        return filtered_items