print("\nWelcome to the Shopping App!\n")

user_name = input("Please enter your first name:\n")
print(f"\n\nHi {user_name}! Welcome to the Shopping App!\n")

item1 = ['Blouse', 89.99, 3]
item2 = ['Boots', 124.49, 1]
item3 = ['Ascot', 215, 2]
item4 = ['Trousers', 349, 5]
item5 = ['Scarf', 79.99, 10]

inventory = [item1, item2, item3, item4, item5]

print("Inventory")
print("************")
for item in inventory:
    print(item[0])
print("************\n")

cart = []
keep_going = 'y'
while keep_going.lower() == 'y':
    user_selection = input("Which item would you like to add to your shopping cart: ")
    for item in inventory:
        if user_selection.lower() in item[0].lower():
            cart.append(user_selection)
    keep_going = input("That's a great choice! Enter 'y' to add another item: ")
else:
    print(f"\n\n{user_name} I bet you'll look amazing in those.\n\n")

print("You've added the following items to your shopping cart")
print("************")
for item in cart:
    print(item.title())
print("************")
