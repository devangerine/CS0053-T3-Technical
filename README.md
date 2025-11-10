# Object-Oriented Food Order System

## 1. Program Overview

This project implements a simple, console-based food order taking system using **Object-Oriented Programming (OOP)** principles in Python. The primary purpose of this application is to demonstrate the effective use of classes and objects to model real-world entities, specifically a menu, menu items, and a customer's order. The system allows a user to select items and quantities from a predefined menu, and it automatically calculates and outputs the total price of the order.

## 2. Development Environment

The system was developed and tested within a sandboxed virtual machine environment.

| Component | Specification |
| :--- | :--- |
| **Programming Language** | Python 3.11.0rc1 |
| **Development Environment** | Command-Line Interface (CLI) in a Linux Sandbox |
| **Key Libraries** | Standard Python Library (No external dependencies) |

## 3. Implementation Process

The system was implemented following a modular, OOP approach, structured around three core classes: `MenuItem`, `Menu`, and `Order`.

### Step 1: Designing the OOP Structure
The design phase established the responsibilities for each class:
*   **`MenuItem`**: Encapsulates the data for a single item (`name` and `price`).
*   **`Menu`**: Acts as a container for all `MenuItem` objects and provides lookup functionality.
*   **`Order`**: Manages the collection of items and quantities for a specific customer, and contains the logic for calculating the total cost.

### Step 2: Implementing Core Classes (`MenuItem` and `Menu`)
The `MenuItem` class was implemented with a simple `__init__` method for initialization. The `Menu` class was implemented to load a set of sample menu items into a dictionary for quick, case-insensitive lookup via the `get_item` method.

### Step 3: Implementing the `Order` Class
The `Order` class uses a dictionary to store the items and their quantities (`{MenuItem: quantity}`). The `add_item` method handles adding new items or incrementing the quantity of existing items. The `calculate_total` method iterates through the stored items, multiplies the price by the quantity for each, and sums the results to return the final total.

### Step 4: Implementing User Interaction Logic
A `main` function was created to handle the application flow:
1.  Initialize `Menu` and `Order` objects.
2.  Display the menu to the user.
3.  Enter a `while True` loop to continuously prompt the user for input.
4.  Input is parsed to separate the item name and quantity.
5.  Error handling (using `try...except`) was implemented to catch invalid quantity inputs (non-integers) and to handle items not found on the menu.
6.  The loop terminates when the user enters the keyword 'done', at which point the final order summary and total price are displayed.

## 4. Testing & Debugging

The system was tested by simulating a typical user order scenario, including successful additions and handling of invalid input.

### Sample Test Run

**Input Sequence:**
1.  `Burger 1` (Successful addition)
2.  `Fries 2` (Successful addition)
3.  `Pizza 1` (Item not found, testing error handling)
4.  `Soda 1` (Successful addition)
5.  `done` (Finalize order)

**Output:**
The final output correctly calculates the total price based on the successful additions.

\`\`\`
--- Order Finalized ---
--- Your Order Summary ---
Burger          x 1  @ $8.99 = $8.99
Fries           x 2  @ $3.49 = $6.98
Soda            x 1  @ $1.99 = $1.99

Total Price:         $17.96
--------------------------
Total Price: $17.96
Thank you for your order!
\`\`\`

**Calculation Verification:**
*   Burger: $8.99 * 1 = $8.99
*   Fries: $3.49 * 2 = $6.98
*   Soda: $1.99 * 1 = $1.99
*   **Total:** $8.99 + $6.98 + $1.99 = **$17.96**

### Errors and Debugging

| Error Encountered | Description and Fix |
| :--- | :--- |
| **Input Parsing Failure** | Initially, the input parsing logic failed when an item name contained spaces (e.g., "Pizza Slice 1"). The original `split()` method was too simple. |
| **Fix** | The parsing logic was updated to use `user_input.rsplit(' ', 1)`, which splits the string only once from the right. This ensures that the last token is always the quantity, and everything before it is treated as the item name, correctly handling multi-word item names. |
| **Case Sensitivity** | The menu lookup was initially case-sensitive, causing items like "burger" to fail if the menu listed "Burger". |
| **Fix** | The `Menu.get_item` method was updated to convert the input item name to lowercase (`item_name.lower()`) before checking the menu dictionary, which stores all keys in lowercase. This made the system more user-friendly by allowing case-insensitive input. |
