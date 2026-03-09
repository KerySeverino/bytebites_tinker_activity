# ByteBites backend model scaffolds
# Classes:
# - Customer: stores a customer's name and purchase history
# - Transaction: stores selected food items and can compute total cost
# - FoodItem: stores information about a menu item
# - Menu: stores all food items and can filter by category


class FoodItem:
    # Represents a single item on the menu (e.g. "Spicy Burger")
    def __init__(self, name, price, category, popularity_rating):
        self.name = name                        # e.g. "Spicy Burger"
        self.price = price                      # e.g. 8.99
        self.category = category                # e.g. "Burgers"
        self.popularity_rating = popularity_rating  # e.g. 4.5


class Menu:
    # Holds all available FoodItems and allows filtering by category
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter_by_category(self, category):
        # Returns a list of items that match the given category
        filtered_items = []
        for item in self.items:
            if item.category == category:
                filtered_items.append(item)
        return filtered_items

    def sort_by_popularity(self):
        # Returns a new list of all items sorted by popularity_rating, highest first
        # sorted() does not modify self.items — the original menu order is preserved
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    # Represents a single order — a group of FoodItems chosen by a customer
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def compute_total(self):
        # Adds up the price of every item in the transaction
        total = 0
        for item in self.selected_items:
            total += item.price
        return total


class Customer:
    # Represents a user of the ByteBites app
    def __init__(self, name, purchase_history=None):
        self.name = name                        # customer's name as a string
        self.purchase_history = purchase_history if purchase_history is not None else []

  