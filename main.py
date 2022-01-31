def print_inventory(inventory):
    print("{:^24}".format("Inventory"))
    print("************************")
    for item in inventory:            
        print ('{:<10} {:<10} {:<10}'.format(f"{item.name}", f"${item.price}", f"{item.quantity}"))
    print("************************")    

def print_shopping_cart(shopping_cart):
    for i in shopping_cart:
        print(i.name)

print("\nWelcome to the Shopping App!\n")

user_name = input("Please enter your first name:\n")
print(f"\n\nHi {user_name}! Welcome to the Shopping App!\n")

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item('Blouse', 89.99, 3)
item2 = Item('Boots', 124.49, 1)
item3 = Item('Ascot', 215, 2)
item4 = Item('Trousers', 349, 5)
item5 = Item('Scarf', 79.99, 10)

inventory = [item1, item2, item3, item4, item5]

print_inventory(inventory)

print()
cart = []
quantity = 0

def add_to_cart(item, cart, quantity):
    item.quantity = item.quantity - quantity
    cart.append(item)

keep_going = 'y'
while keep_going.lower() == 'y':
    user_selection = input("\nWhich item would you like to add to your shopping cart: ")
    quantity = int(input("\nHow many would you like? "))
    for item in inventory:
        if user_selection.lower() in item.name.lower() and quantity <= item.quantity:
            add_to_cart(item, cart, quantity)

    keep_going = input("\nThat's a great choice! Enter 'y' to add another item: ")
else:
    print(f"\n\n{user_name} I bet you'll look amazing in those.\n\n")

print(f"You've added the following items to your shopping cart")
print_shopping_cart(cart)
print()

def remove_from_inventory(cart, inventory):
    for item in inventory:
        item.quantity = item.quantity - 1
    return inventory
    
tax = 0

def get_total(cart, quantity):
    sum = 0.0
    for item in cart:
        sum += item.price * (quantity)
    tax = sum * .06
    total = "${:,.2f}".format(sum + tax)
    return total

total = get_total(cart, quantity)

print(f"Your total with tax is {total}.")
print()

print_inventory(inventory)
