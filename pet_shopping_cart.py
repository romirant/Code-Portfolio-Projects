'''


'''


def add_item(x,y):
    """Add items to my cart."""
    item = input("Please enter the name of the item you would like to add: ")
    cost = float(input("Please enter the price of that item: £"))
    x.append(item)
    y.append(cost)
    print(f"\n{item} has been added to your cart successfully!")
    print("-"*80)


def view_items(x):
    """View items in shopping list."""
    for i, item in enumerate(x, 1):
            print(i, item)

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



items = ["Cat Food", "Dog Food", "Dog Bed", "Toys"]
stock = {"Cat Food": 15, "Dog Food": 15, "Dog Bed": 10, "Cat Toys": 20}
prices = {"Cat Food": 7.50, "Dog Food": 5.70, "Dog Bed": 15, "Cat Toys": 3.40}
cart = []
cost_list = []
border = "-"*80
welcome = "Welcome to the Pets-R-Us Shop!"

print(border)
print(welcome)
print(border)


while True:
    # Ask user to select an option form the menu
    menu = input("Please select an option below:\n1: Add item\n2: View List"\
                "\n3: Delete item\n4: Sort List\n0: Exit\n"\
                    "\nI would like to: ")
    print(border)
    if menu == "1":
        add_item(cart,cost_list)
    elif menu == "2":
        view_items(cart)
    elif menu == "3":
        delete_item(cart)
    elif menu == "4":
        sort_items(cart)
    elif menu == "0":
        # Exit program
        print("Goodbye!")
        break
    else:
        print("\n")
        print("That is not a valid option")
        print("-"*80)


