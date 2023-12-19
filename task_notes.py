'''
Challenge:
Develop a shopping cart application, called Paws n Cart,
for pet related products to help manage your products and
that can provide information on adoption centres and care advice


Objective: Develop a program to:
- create a shopping cart for a user which they can view
- Allow users to add and remove items from their cart
- Calculate the total cost of the cart when requested

Code Toolbox
- adding items to a list
#using string concatenation to create lists
    list = "Orange"
    list += ",Apple"
    list += ",Chair"
    list += ",Pear"

- removing items from a list
#finding and removing a piece of a string
remove = "Chair"
occurence = list.find(remove)

if occurence == 0:
    list = list[:len(remove)+1]
else:
    list = list[:occurence-1] + list[occurence+len(remove):]

- Displaying a list of items
done = False
pointer = 0
counter = 1

#Find the next occurence for the , by specifying the start value
# Print items in the list formatted neatly

while (not done):
    index = list.find(",", pointer)

    if (index == -1):
        done = True
        index = len(list)

    print("Item {:2}: \t {}".format(counter, list[pointer:index]))
    pointer = index + 1
    counter += 1

- Display menu continuously

done = Fasle
while (not done):
    print("\n")
    print("-"*80)

Implementing different menu options

In if code

if choice == "1":
    item = input("What would you like to add to your cart: ")
    price = 

'''

'''
Step by step Tasks:
1. Data structure: create variables that will stroe the items and their prices. In lists or strings
2. User Menu: Create a suer menu that displays the cart to the users
3. Manipulating the cart: add and remove items
4. Calculating total cost: calculate the cost at the end

Advanced:
1. Allow users to change the quantity of each item
2. Add functionality to your programme that will offer users personalised suggesstions based on products in their cart
3. Create a llist of products that will be displayed to the user and suers will have to choose items from this list only
'''