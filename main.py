# Menu dictionary - prices in rupees
menu = {
    "samosa": 80,
    "salted popcorn": 100,
    "caramel popcorn": 120,
    "cheese popcorn": 150,
    "schezwan fries": 150,
    "cheese nachos": 160,
    "loaded burger": 180,
    "farmhouse pizza": 180,
    "ice cream": 100,
    "hot chocolate": 120,       
    "chocolate milkshake": 150,
    "strawberry milkshake": 150,
    "soda": 120,
    "lemonade": 100,
    "cold coffee": 100,
    "coffee": 80,
    "iced tea": 80,
    "coke": 70,
    "pepsi": 70,
    "water": 20
}


def display_menu(menu_dict):
    """
    Displays the restaurant menu in a formatted table.
    
    Parameters:
        menu_dict (dict): Dictionary containing menu items and their prices
    
    Returns:
        None
    """
    print("-------------------MENU-------------------")
    for item, price in menu_dict.items():
        # Format: item name (30 chars wide) : price with 2 decimal places
        print(f"{item:30} : ₹{price:.2f}")
    print("------------------------------------------\n")


def get_user_orders(menu_dict):
    """
    Takes orders from the user until they finish or quit.
    
    Parameters:
        menu_dict (dict): Dictionary containing available menu items
    
    Returns:
        list: List of ordered items, or empty list if user quits without ordering
    """
    cart = []
    
    while True:
        order = input("Enter your order (f to finish): ").lower().strip()
        
        # User wants to finish ordering
        if order == "f":
            break
        
        # User entered nothing (empty input)
        elif order == "":
            print("You have not ordered anything.")
            print("Thank You! Have a great day 😊❤️")
            return []  # Return empty cart
        
        # Check if item exists in menu
        elif order in menu_dict:
            cart.append(order)
            print(f"✓ {order.title()} added to cart!")
        
        # Item not found in menu
        else:
            print("Sorry! That item is not on the menu.")
    
    return cart


def calculate_total(cart, menu_dict):
    """
    Calculates the total price of all items in the cart.
    
    Parameters:
        cart (list): List of ordered items
        menu_dict (dict): Dictionary containing menu items and prices
    
    Returns:
        float: Total price of all items in cart
    """
    total = 0
    for item in cart:
        total += menu_dict[item]
    return total


def display_order_summary(cart, menu_dict):
    """
    Displays a summary of the order with itemized prices and total.
    
    Parameters:
        cart (list): List of ordered items
        menu_dict (dict): Dictionary containing menu items and prices
    
    Returns:
        None
    """
    if not cart:  # If cart is empty, don't display anything
        return
    
    print("\n----------------YOUR ORDER----------------")
    for item in cart:
        print(f"{item:20} : ₹{menu_dict[item]}")
    print("------------------------------------------\n")
    
    # Calculate and display total
    total = calculate_total(cart, menu_dict)
    print(f"Your total price is: ₹{total}")
    print("Thank You! Have a great day 😊❤️")


def main():
    """
    Main function that orchestrates the restaurant ordering system.
    Displays menu, takes orders, and shows the final bill.
    
    Returns:
        None
    """
    # Display the menu to the customer
    display_menu(menu)
    
    # Get all orders from the user
    cart = get_user_orders(menu)
    
    # Display order summary and total (only if cart has items)
    display_order_summary(cart, menu)


# Run the program
if __name__ == "__main__":
    main()