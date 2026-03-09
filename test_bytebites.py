import pytest
from models import Customer, FoodItem, Transaction, Menu


# Verify that a transaction with multiple items returns the correct total.
def test_calculate_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 10.00, "Entree", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)

    transaction = Transaction([burger, soda])

    assert transaction.compute_total() == 15.00


# Verify that an empty transaction returns a total of 0.
def test_order_total_is_zero_when_empty():
    transaction = Transaction()

    assert transaction.compute_total() == 0


# Verify that filtering by category returns only matching menu items.
def test_filter_menu_items_by_category():
    burger = FoodItem("Spicy Burger", 10.00, "Entree", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    juice = FoodItem("Orange Juice", 4.00, "Drinks", 4.5)
    cake = FoodItem("Chocolate Cake", 6.00, "Desserts", 4.9)

    menu = Menu([burger, soda, juice, cake])

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert drinks[0].name == "Large Soda"
    assert drinks[1].name == "Orange Juice"
    
def test_sort_menu_by_popularity():
    burger = FoodItem("Spicy Burger", 10.00, "Entree", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.00, "Desserts", 4.9)

    menu = Menu([burger, soda, cake])

    sorted_items = menu.sort_by_popularity()

    assert sorted_items[0].name == "Chocolate Cake"
    assert sorted_items[1].name == "Spicy Burger"
    assert sorted_items[2].name == "Large Soda"