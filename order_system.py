class MenuItem:
    """Represents a single item on the menu."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

class Menu:
    """Manages the collection of available menu items."""
    def __init__(self):
        self.items = {}
        self._load_menu()

    def _load_menu(self):
        """Populates the menu with sample items."""
        menu_data = [
            ("Burger", 8.99),
            ("Fries", 3.49),
            ("Soda", 1.99),
            ("Salad", 7.50),
            ("Pizza Slice", 4.00)
        ]
        for name, price in menu_data:
            self.items[name.lower()] = MenuItem(name, price)

    def display_menu(self):
        """Prints the available menu items and their prices."""
        print("\n--- Menu ---")
        for item in self.items.values():
            print(f"{item.name:<15} ${item.price:.2f}")
        print("------------")

    def get_item(self, item_name: str) -> MenuItem | None:
        """Retrieves a MenuItem object by its name (case-insensitive)."""
        return self.items.get(item_name.lower())

class Order:
    """Manages the items added to a customer's order and calculates the total cost."""
    def __init__(self):
        # Stores {MenuItem: quantity}
        self.items = {}

    def add_item(self, menu_item: MenuItem, quantity: int):
        """Adds a specified MenuItem and quantity to the order."""
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return

        if menu_item in self.items:
            self.items[menu_item] += quantity
        else:
            self.items[menu_item] = quantity
        print(f"Added {quantity} x {menu_item.name} to the order.")

    def calculate_total(self) -> float:
        """Calculates and returns the total price of all items in the order."""
        total = 0.0
        for item, quantity in self.items.items():
            total += item.price * quantity
        return total

    def display_order(self):
        """Prints a summary of the current order."""
        if not self.items:
            print("The order is empty.")
            return

        print("\n--- Your Order Summary ---")
        total_cost = 0.0
        for item, quantity in self.items.items():
            line_total = item.price * quantity
            total_cost += line_total
            print(f"{item.name:<15} x {quantity:<2} @ ${item.price:.2f} = ${line_total:.2f}")

        print(f"\n{'Total Price:':<20} ${total_cost:.2f}")
        print("--------------------------")

# The main execution logic will be added in the next phase.

def main():
    """Main function to run the food order system."""
    menu = Menu()
    order = Order()

    print("Welcome to the OOP Food Order System!")
    menu.display_menu()

    while True:
        print("\nEnter an item name and quantity (e.g., 'Burger 2'), or 'done' to finish, or 'menu' to see the menu again.")
        user_input = input("> ").strip()

        if user_input.lower() == 'done':
            break
        elif user_input.lower() == 'menu':
            menu.display_menu()
            continue

        try:
            parts = user_input.rsplit(' ', 1)
            if len(parts) < 2:
                print("Invalid input format. Please enter item name and quantity (e.g., 'Fries 1').")
                continue

            item_name_raw = parts[0].strip()
            quantity = int(parts[1].strip())

            menu_item = menu.get_item(item_name_raw)

            if menu_item:
                order.add_item(menu_item, quantity)
            else:
                print(f"Item '{item_name_raw}' not found on the menu. Please check the spelling.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number for the quantity.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Final output
    print("\n--- Order Finalized ---")
    order.display_order()
    print(f"Total Price: ${order.calculate_total():.2f}")
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
