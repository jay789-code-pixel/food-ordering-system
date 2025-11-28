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
    print("-------------------MENU-------------------")
    for item, price in menu_dict.items():
        print(f"{item:30} : ₹{price:.2f}")
    print("------------------------------------------\n")


def get_user_orders(menu_dict):

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
    total = 0
    for item in cart:
        total += menu_dict[item]
    return total


def display_order_summary(cart, menu_dict):

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

    # Display the menu to the customer
    display_menu(menu)
    
    # Get all orders from the user
    cart = get_user_orders(menu)
    
    # Display order summary and total (only if cart has items)
    display_order_summary(cart, menu)


# Run the program
if __name__ == "__main__":

    main()
