cart = []
total = 0
menu = {
        "samosa" : 80,
        "salted popcorn" : 100,
        "caramel popcorn" : 120,
        "cheese popcorn" : 150,
        "schezwan fries" : 150,
        "cheese nachos" : 160,
        "loaded burger" : 180,
        "farmhouse pizza" : 180,
        "ice cream" : 100,
        "hot chocolate" : 120,       
        "chocolate milkshake" : 150,
        "strawberry milkshake" : 150,
        "soda" : 120,
        "lemonade" : 100,
        "cold coffee" : 100,
        "coffee" : 80,
        "iced tea" : 80,
        "coke" : 70,
        "pepsi" : 70,
        "water" : 20
}


print("-------------------MENU-------------------")

for key, value in menu.items():
    print(f"{key:30} : ₹{value:.2f}")

print("------------------------------------------")
print()



while True:

    order = input("Enter your order (f to finish): ").lower().strip()

    if order == "f":
        break
    elif menu.get(order) is not None:
        cart.append(order)
    else:
        print("Sorry! that order is not present in menu. ")

for order in cart:
    total += menu.get(order)

if len(cart) != 0:

    
    print("\n----------------YOUR ORDER----------------")
    for item in cart:
        print(f"{item:20} : {menu.get(item)}")
    print("------------------------------------------\n")
    print()

    print(f"Your total price is: ₹{total}")
    print("Thank You! Have a great day 😊❤️")

else:
    print("You haven't ordered anything. ")
    print("Thank You! Have a great day 😊❤️")
