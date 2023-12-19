menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0.0
#a while like the one in dors coding school, not quite the same, but the while True they used as proven to be very useful
#as is, it is quite long, it could be made shorter, but still, as long as it can add items together and reprompt as needed then we gucci
while True:

    try:
        item = input("Item (type 'exit' to quit): ").title()

        if item == "Exit":
            break

        if item in menu:

            total_price += menu[item]

            print(f"Total: ${total_price:.2f}")

        else:
            print("Item not found in the menu.")

    except EOFError:
        print()
        break