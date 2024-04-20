import datetime

class OrderItem:
    # List of item (details) available 
    _item_list = [
        [1001, "Sprite", 2.20, 5, 0],
        [1002, "Coke", 2.50, 10, 0],
        [1003, "Mountain dew", 1.90, 15, 0],
        [1004, "Monster", 5.40, 18, 0],
        [1005, "100 plus", 1.80, 5, 0],
        [1006, "Fanta", 2.80, 10, 0],
        [1007, "7up", 3.30, 15, 0],
        [1008, "Sparkling", 4.60, 12, 0]
    ]

    # initializing item attributes
    def __init__(self, item_id, product, unit_price, discount, qty):
        self._product = product
        self._unit_price = unit_price
        self._discount = discount
        self._qty = qty

        self._item_id = item_id

    # Method to set quantity
    def set_qty(self, newQty):
        self._qty = newQty

    # Method to get item id
    def get_item_id(self):
        return self._item_id
    
    # Method to get total amount
    def get_total_amount(self):
        return self._unit_price * self._qty
    
    # Method to get discount amount
    def get_discount_amount(self):
        return self.get_total_amount() * (self._discount / 100)
    
    # Method to get actual amount
    def get_actual_amount(self):
        return self.get_total_amount() - self.get_discount_amount()
    
    # Method to return a string representation of the item
    def __str__(self):
        return f"Item Id: {self._item_id} || Item: {self._product} || Quantity: {self._qty} || Amount(SGD): {self.get_actual_amount():.2f}$"

class CustOrder:
    _NEXT_ID_1 = 101

    # initializing item attributes
    def __init__(self, recipient, address):
        self._recipient = recipient
        self._address = address
        self._date_ordered = datetime.date.today()
        self._items = []

        self._ref_no = CustOrder._NEXT_ID_1
        CustOrder._NEXT_ID_1 += 1
    
    # Method to get reference number
    def get_ref_no(self):
        """ Return this note's unique id. """
        return self._ref_no
    
    # Method to add an item to the order
    def add_item(self, item):
    # Check if any item with the same item_id is already in the order
        for existing_item in self._items:
            if existing_item.get_item_id() == item.get_item_id():
                print("Item already in order\n")
                # If an item with the same item_id exists, do not add it again
                return False
            
        # If the item with the same item_id is not found, add the new item
        self._items.append(item)
        print("Item added to order\n")
        return True
        
    # Method to remove item from the order
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print("Item has been removed from the order successfully")
            return True
        
        else:
            # print("Item has been already removed.")
            return False
        
    # Method to calculate the actual amount after discount for the item
    def get_total(self):
        total = 0
        for item in self._items:
            total += item.get_actual_amount()
        return total
    
    # Method to return a string representation of the order
    def __str__(self):
        ord_details = ""
        for item in self._items:
            ord_details += str(item) + "\n"
            
        return f'''=========================== Customer Order ===========================
Order Number: {self._ref_no},
Recipient: {self._recipient}, 
Day of Order: {self._date_ordered}
Total Amount(SGD): {self.get_total():.2f}$, 
Order Details: 
{ord_details}
----------------------------------------------------------------------'''
    
# Method to display the main menu options and return the user's choice.
def main_menu():
    print("Main Menu: \n")
    print("1. Display all orders")
    print("2. Display all drinks")
    print("3. Place order")
    print("4. Configure order")
    print("5. Exit")
    return input("Enter an option: ")

# Method to diplay all available drinks with their details.
def display_products(items):
    print("Available Drinks:")
    for item_info in items._item_list:
        print(f"Id: {item_info[0]} || {item_info[1]} || Price: {item_info[2]:.2f}$")

    # Method to add new order 
def add_order(orders):
    recipient_name = input("Enter Name: ")
    recipient_address = input("Enter Address: ")
    new_ord = CustOrder(recipient_name, recipient_address)
    orders.append(new_ord)
    while True:
        item_name = input("Enter product name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_found = False
        for item_info in OrderItem._item_list: 
            if item_info[1].lower() == item_name.lower():
                while True:
                    item_qty = input("Enter product quantity: ")
                    if item_qty.isdigit():
                        item_qty = int(item_qty)
                        new_item = OrderItem(item_info[0], item_info[1], item_info[2], item_info[3], item_qty)
                        new_ord.add_item(new_item)
                        # print("Item added to order.\n")
                        item_found = True
                        break
                    else:
                        print("Invalid input. Enter product quantity: ")
        if not item_found:
            print("Product not found.")
    print("Order added successfully.")
    
    # Method to access an exiting order by order id
def access_order(orders):
      while True:
        order_found = False 
        access_id = input("Enter Order Id: ")
        for order in orders:
            if access_id == str(order.get_ref_no()):
                    print("Order found")
                    print(order)
                    access_item(order)
                    order_found = True
                    break
        if order_found:
            break
        else:
            print("Order not found. Please Try again...")

    # Method to access an existing item in an existing order by item id
def access_item(order):
    while True:
        item_found = False 
        access_item_id = input("Enter Item Id: ")
        for item in order._items:
            if access_item_id == str(item.get_item_id()):
                print("Item found")
                print(item)
                item_found = True
                config_item(order, item)
                break
        if item_found:
            break
        else:
            print("Item not found. Please Try again...")

    # Method to configure item in an order (add or remove quantity)
def config_item(order, item):
    while True:
        add_remove_choice = input("Enter 'A' to add or 'R' to remove the item: ").strip().upper()
        if add_remove_choice == "A":
            quantity = int(input("Enter quantity to be added: "))
            item._qty += quantity
            print("Item has been updated successfully.")
            print("Updating order details...")
            break 
        elif add_remove_choice == "R":
            quantity = int(input("Enter quantity to be removed: "))
            if quantity <= item._qty:  
                item._qty -= quantity
                if item._qty == 0:
                    order.remove_item(item)
                print("Item has been updated successfully.")
                print("Updating order details...")
                break  
            else:
                print("Quantity to be removed exceeds the available quantity.")
        else:
            print("Invalid option. Please enter 'A' to add or 'R' to remove: ")

    # Main function to run the program
def main():
    orders = []
    
    while True:
        option = main_menu()
        if option == "1":
            for order in orders:
                print(order)
        elif option == "2":
            display_products(OrderItem)
        elif option == "3":
            add_order(orders)
        elif option == "4":
            access_order(orders)
        elif option == "5":
            break
        else:
            print("Invalid Option....")

    print("Thank you")

if __name__ == "__main__":
    main()
