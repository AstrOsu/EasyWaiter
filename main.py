import time
class Table(object):
    orders = []
    waiter = None #need to make a waiter class to store here

    def __init__(self, id, seating):
        self.id = id
        self.seating = seating    
    
    def add_order(self, MenuItem):
        self.orders.append(MenuItem)

    def total_bill(self):
        pass #add up the price of all MenuItems in orders[]

    def clear_table(self):
        orders = []

    
class Menu(object):
    foodItems = []

    def __init__(self):
        pass #needs to read the menu from a file

    def add_item(self, MenuItem):
        self.foodItems.append(MenuItem)

class MenuItem(object):
    def __init__(self, name, price, mealType):
        self.name = name
        self.price = price
        self.mealType = mealType #app, entree, dessert, drink, etc.


#testmenu = Menu()
#testmenu.add_item(MenuItem("banana", 1, "snack"))

#print(testmenu.foodItems[0])

#time.sleep(50)