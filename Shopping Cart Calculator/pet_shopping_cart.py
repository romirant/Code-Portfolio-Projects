'''


'''
class Item:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

# def add_item(x, p_dict, s_dict):
#     """Add items to my cart."""

#     # Display available items
#     while True:
#         for key, value in p_dict.items():
#             item_stock = s_dict.get(key, 0)  # Get stock level, default to 0 if not found
#             print(f"{key}:\t£{value}\tStock: {item_stock}")

#         # Ask the user for the item they want to add
#         item = input("Enter the name of the item you would like to add (or -1 to return to the menu): ")

#         if int(item) == -1:
#             break
#         else:
#             # Convert the item to title case (sentence case for multi-word strings)
#             item = item.title()

#             # Check if the item is in the product dictionary and in stock
#             if item in p_dict and s_dict.get(item, 0) > 0:
#                 # Ask for the quantity
#                 quantity = input(f"How many of {item} would you like to add? ")
#                 try:
#                     quantity = int(quantity)
#                     # Check if the requested quantity is available
#                     if quantity <= s_dict[item]:
#                         # Add the item and quantity to the cart
#                         x.append((item, quantity))
#                         # Update the stock dictionary
#                         s_dict[item] -= quantity
#                         print(f"\n{quantity} of {item} have been added to your cart successfully!\n" + "-"*80)
#                         break
#                     else:
#                         print(f"\nWe do not have enough stock for {quantity} of {item}. Please try a smaller amount.\n")
#                 except ValueError:
#                     print("\nPlease enter a valid number for the quantity.\n")
#             else:
#                 print("\nI'm sorry but that item is not available or out of stock, please try again\n" + "-"*80)

def validate_string_input(prompt):
    while True:
        value = input(prompt)
        if value.isalpha():
            return value
        else:
            print("\nInvalid input. Please enter a valid string value.")

def validate_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value > 0:
                return value
            else:
                print("\nInvalid input. Please enter a positive float value.")
        except ValueError:
            print("\nInvalid input. Please enter a valid float value.")

def validate_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value > 0:
                return value
            else:
                print("\nInvalid input. Please enter a positive value.")
        except ValueError:
            print("\nInvalid input. Please enter a valid integer value.")

def choice_validation():
    while True:
        choice = input("\nEnter your choice (y/n) or -1 to go back to the main menu: ")
        if choice.lower() == "y" or choice.lower() == "n":
            return choice
        elif choice == "-1":
            return -1
        else:
            print("\nInvalid choice. Please choose y/n or -1")

def add_item():

    name = validate_string_input("\nWhat is the item you would to add to your cart: ")
    while True:
        print(f"\nYou have added {name}, is that correct?")
        name_check = choice_validation()
        match name_check:
            case "y":
                name = name.title()
                break
            case "n":
                name = validate_string_input("\nWhat is the item you would to add to your cart: ")
                continue
            case -1:
                return


    cost = validate_float_input("\nWhat is the cost of the item: £")
    while True:
        print(f"\nThe cost is £{cost:.2f}, is that correct?")
        cost_check = choice_validation()
        match cost_check:
            case "y":
                cost = float(cost)
                break
            case "n":
                cost = validate_float_input("\nWhat is the cost of the item: £")
                continue
            case -1:
                return


    quantity = validate_int_input("\nHow many of the item would you like to add: ")
    while True:
        print(f"\nYou would like to add {quantity}, is that correct?")
        quantity_check = choice_validation()
        match quantity_check:
            case "y":
                break
            case "n":
                quantity = validate_int_input("\nHow many of the item would you like to add: ")
                continue
            case -1:
                return


    new_item = Item(name, cost, quantity)
    cart.append(new_item)



def view_items(x):
    """View items in shopping list."""
    while True:
        if x == []:
            print("\nYour cart is empty")
            break
        else:
            for i, item in enumerate(x, 1):
                print(i, item)
                break

def delete_item(x):
    """Delete item from shopping list."""
    for i, item in enumerate(x, 1):
        print(i, item)
        index = input("Please enter the index of the item you would like to remove:\n")
        index = int(index)-1
        item = x[index]
        x.pop(index)
        print(f'{item} has been removed from your cart!')

def sort_items(x):
    """Sort shopping list."""
    x.sort()
    print("List sorted!")

def total_cost(x,p_dict):
    '''Find total of cart'''
    total_price = 0
    for item in x:
        total_price += p_dict.get(item)
    print(f"Your total is: £{total_price}")




items = ["Cat Food", "Dog Food", "Dog Bed", "Toys"]
stock = {"Cat Food": 15, "Dog Food": 15, "Dog Bed": 10, "Cat Toys": 20}
prices = {"Cat Food": 7.50, "Dog Food": 5.70, "Dog Bed": 15, "Cat Toys": 3.40}
cart = []
cost_list = []
border = "-"*80
welcome = "Welcome to the Pets-R-Us Shop!"






print(border + "\n" + welcome + "\n" + border)



while True:
    # Ask user to select an option form the menu
    menu = input("\nPlease select an option below:\n1: Add item\n2: View List"\
                "\n3: Delete item\n4: Sort List\n5: Total Cost\n0: Exit\n"\
                    "\nI would like to: ")
    print(border)

    match menu:
        case "1":
            add_item()
        case "2":
            view_items(cart)
        case "3":
            delete_item(cart)
        case "4":
            sort_items(cart)
        case "5":
            total_cost(cart, prices)
        case "0":
            #Exit program
            print("Goodbye!")
            break
        case _:
            print("\nThat is not a valid option\n" + "-"*80)
