
def print_inventory(inventory):
    for item in inventory:            
        print(f"{item.name}  ${item.price}  {item.quantity}")
        

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

print("Inventory")
print("************")
print_inventory(inventory)

print()
cart = []
quantity = 0

def add_to_cart(item, cart, quantity):
    item.quantity = item.quantity - quantity
    cart.append(item)

keep_going = 'y'
while keep_going.lower() == 'y':
    user_selection = input("Which item would you like to add to your shopping cart: ")
    quantity = int(input("How many would you like? "))
    for item in inventory:
        if user_selection.lower() in item.name.lower():
            add_to_cart(item, cart, quantity)

    keep_going = input("That's a great choice! Enter 'y' to add another item: ")
else:
    print(f"\n\n{user_name} I bet you'll look amazing in those.\n\n")

print("You've added the following items to your shopping cart")

print_shopping_cart(cart)
print()

def remove_from_inventory(cart, inventory):
    for item in inventory:
        item.quantity = item.quantity - 1
        # for i in cart:
        #     if item in cart:
        #         item.quantity = item.quantity - i.quantity
    return inventory


tax = 0

def get_total(cart, quantity):
    sum = 0
    for item in cart:
        sum = sum + item.price(quantity)
    tax = sum * .06
    total = sum + tax
    return total

total = get_total(cart, quantity)

print(f"Your total with tax is ${total}.")
print()

# remove_from_inventory(cart, inventory)
print_inventory(inventory)
