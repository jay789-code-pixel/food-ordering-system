Project Overview
A simple command-line based food ordering system designed for a movie theater or café environment. 
The application allows customers to browse a menu, place orders, and receive a bill summary.

Features

Menu Display:

Comprehensive menu with 20 food and beverage items
Items categorized into snacks, meals, and beverages
Price range: ₹20 to ₹180
Clean, formatted display with proper alignment

Order Management:

Interactive ordering process with continuous input loop
Real-time order validation against menu items
Error handling for invalid orders
Case-insensitive input for user convenience
Ability to order multiple items

Billing System:

Automatic total calculation
Itemized bill generation
Handles empty orders gracefully
Professional receipt format

Technical Implementation:

Data Structures
Dictionary (menu) = Stores item names and prices for efficient lookup
List (cart) = Maintains ordered items in sequence

Key Functions Used:

menu.get(): Safe dictionary access with None return for missing items
Input validation: Loop-based order entry with exit condition

User Experience:

Customer views formatted menu
Enters items one by one using item names
Types 'f' to complete order
Receives itemized bill with total amount

Conclusion
This project demonstrates fundamental programming concepts including data structures, loops, conditionals, and user input handling. 
It provides a functional solution for simple food ordering scenarios with room for future expansion.
