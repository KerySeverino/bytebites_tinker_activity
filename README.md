# ByteBites Tinker Activity

This project implements a simple backend model for the ByteBites app using Python.

The system includes four main classes:
- **Customer** – stores customer information and purchase history
- **FoodItem** – represents menu items with name, price, category, and popularity rating
- **Transaction** – groups selected items and computes the total cost
- **Menu** – manages the collection of food items and supports filtering and sorting

Key features implemented:
- Filter menu items by category
- Sort menu items by popularity
- Compute the total cost of a transaction

Pytest tests are included to verify:
- transaction total calculations
- empty transaction totals
- category filtering behavior

This project was built using an AI-assisted workflow with Copilot for planning, drafting, and refining the implementation.
