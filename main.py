Certainly! Below is a Python program for "Eco-Shopper," an intelligent shopping assistant designed to optimize grocery lists for sustainability and budget. This program focuses on helping users reduce food waste and manage expenses effectively. It provides features like suggesting sustainable products, tracking budgets, and offering tips to reduce food waste. Additionally, error handling is included for robust performance.

```python
import json

class EcoShopper:
    def __init__(self, budget):
        self.budget = budget
        self.grocery_list = {}
        self.product_database = self.load_product_database()
        self.sustainable_tips = [
            "Buy in-season produce to support local farmers.",
            "Avoid single-use plastics; bring your own bags.",
            "Plan meals before shopping to reduce impulse buys.",
            "Store food properly to maintain freshness longer."
        ]

    def load_product_database(self):
        # Emulates loading a database; a mock list of products with prices and sustainability scores
        return {
            "apple": {"price": 1.0, "sustainable": True},
            "banana": {"price": 0.5, "sustainable": True},
            "beef": {"price": 5.0, "sustainable": False},
            "milk": {"price": 1.5, "sustainable": True},
            "bread": {"price": 2.0, "sustainable": True}
        }

    def add_to_list(self, item, quantity):
        try:
            if item not in self.product_database:
                raise ValueError(f"{item} is not available in the product database.")
            if quantity <= 0:
                raise ValueError("Quantity should be a positive integer.")
            item_info = self.product_database[item]
            self.grocery_list[item] = {
                "quantity": quantity,
                "total_price": item_info['price'] * quantity,
                "sustainable": item_info['sustainable']
            }
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_total_cost(self):
        return sum(item['total_price'] for item in self.grocery_list.values())

    def is_within_budget(self):
        total_cost = self.calculate_total_cost()
        return total_cost <= self.budget

    def suggest_sustainable_alternatives(self):
        alternatives = []
        for item in self.grocery_list:
            if not self.grocery_list[item]['sustainable']:
                alternatives.append(
                    f"Consider reducing consumption of {item} for more sustainable options."
                )
        return alternatives

    def display_shopping_list(self):
        print("\nGrocery List:")
        for item, details in self.grocery_list.items():
            print(f"- {item}: {details['quantity']} (Total: ${details['total_price']:.2f})")
        print(f"\nTotal Cost: ${self.calculate_total_cost():.2f}")
        print(f"Within Budget: {'Yes' if self.is_within_budget() else 'No'}")
        print("\nSustainable Alternatives:")
        for tip in self.suggest_sustainable_alternatives():
            print("- ", tip)

        print("\nEco-friendly Tips:")
        for tip in self.sustainable_tips:
            print("- ", tip)

def main():
    try:
        budget = float(input("Enter your budget for groceries: $"))
        if budget <= 0:
            raise ValueError("Budget should be a positive number.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    shopper = EcoShopper(budget)
    
    print("\nAvailable products:", list(shopper.product_database.keys()))
    
    while True:
        item = input("\nEnter a product to add to the list (or 'done' to finish): ").lower()
        if item == 'done':
            break
        try:
            quantity = int(input(f"Enter the quantity for {item}: "))
            shopper.add_to_list(item, quantity)
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")

    shopper.display_shopping_list()

if __name__ == "__main__":
    main()
```

### Key Features:
- **Budget Tracking**: Users input their budget and the program checks if their shopping list is within that budget.
- **Product Database**: A simple dictionary to emulate a product database with prices and sustainability information.
- **Sustainability Tips**: Provides tips to help users shop more sustainably.
- **Error Handling**: The program gracefully handles errors such as invalid product entries and incorrect input types.

### Usage:
- Run the program, input your budget, and add items by name and quantity. The available products are listed initially.
- The program will display the shopping list, the total cost, and whether the list is within the budget.
- It also suggests alternatives for non-sustainable items and provides general tips for eco-friendly shopping habits.