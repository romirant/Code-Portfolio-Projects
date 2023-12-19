

border = "-"*80
welcome = "Welcome to the Pets-R-Us Shop!"
main_menu = '''
Shop by Pet:
1) Dogs
2) Cats
3) Small Animal
4) Fish
'''
sub_menu = '''
Browse by:
1) Food
2) Beds
3) Toys
'''

print(border)
print(welcome)
print(border)

print(main_menu)

print(border)
main_menu_choice = input("Please choose a number from the options in the menu above: ")
print(border)

while main_menu_choice == (""):
    print(main_menu)
    main_menu_choice = input("You have not made a valid choice.\nPlease choose a number from the menu above or Q to exit the shop: ")
    
