Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {today_date}")
    cart = ShoppingCart(customer_name, today_date)
    while True:
        print_menu(cart)

        
Enter customer's name:
Gabriela Johnson
Enter today's date:
March 10 2024
Customer name: Gabriela Johnson
Today's date: March 10 2024

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Hershey Bar
Enter the item description: Milk Chocolate
Enter the item price: 1.59
Enter the item quantity: 2

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Hershey Bar

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Wine
Enter the item description: Cabernet Sauvignon
Enter the item price: 99.00
Enter the item quantity: 7

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c
Enter the item name to modify: Wine
Enter the new quantity: 3
Traceback (most recent call last):
  File "<pyshell#62>", line 8, in <module>
    print_menu(cart)
  File "<pyshell#53>", line 24, in print_menu
    item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
TypeError: ItemToPurchase.__init__() got an unexpected keyword argument 'quantity'


class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    customer_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {today_date}")
    cart = ShoppingCart(customer_name, today_date)
    while True:
        print_menu(cart)

        
if __name__ == "__main__":
    main()

    
Enter customer's name:
Gabriela Johnson
Enter today's date:
March 10 2023
Customer name: Gabriela Johnson
Today's date: March 10 2023

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Hershey Bar
Enter the item description: Milk Chocolate
Enter the item price: 1.67
Enter the item quantity: 9
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    main()
  File "<pyshell#80>", line 8, in main
    print_menu(cart)
  File "<pyshell#71>", line 16, in print_menu
    item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
  File "<pyshell#67>", line 7, in __init__
    self.quantity = quantity
NameError: name 'quantity' is not defined
NameError: name 'quantity' is not defined
SyntaxError: invalid syntax


class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="March 10, 2024"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, item_quantity=new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    customer_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {today_date}")
    cart = ShoppingCart(customer_name, today_date)
    
    # Adding existing items to the cart
    item1 = ItemToPurchase("Wine", "Cabernet Sauvignon", 99.00, 2)
    item2 = ItemToPurchase("Snickers", "Original", 1.50, 5)
    item3 = ItemToPurchase("Eggs", "Cage Free", 8.00, 1)
    cart.add_item(item1)
...     cart.add_item(item2)
...     cart.add_item(item3)
...     while True:
...         print_menu(cart)
... 
...         
>>> if __name__ == "__main__":
...     main()
... 
...     
Enter customer's name:
Gabriela Johnson
Enter today's date:
March 10 2024
Customer name: Gabriela Johnson
Today's date: March 10 2024

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Hershey Bar
Enter the item description: Milk Chocolate
Enter the item price: 2.55
Enter the item quantity: 4

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Wine

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c
Enter the item name to modify: Hershey Bar
Enter the new quantity: 2

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
