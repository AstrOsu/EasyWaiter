import time
class Table(object):
    orders = []
    orderStatus = None
    waiter = None #need to make a waiter class to store here

    def __init__(self, id, seating):
        self.id = id
        self.seating = seating    
    
    def add_order(self, MenuItem, orderID):
        self.orders.append([MenuItem, orderID])

    def total_bill(self):
        pass #add up the price of all MenuItems in orders[]

    def clear_table(self):
        orders = []

    def place_order(self, orderID):
        pass #Make the proper call to the KanBan board

    
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

class KanBan(object):
    toDo = None
    inProgress = None
    finished = None

    def add_order(self, Table, order):
        pass
    def start_item(self):
        pass
    def finish_item(self):
        pass

class Staff(object):
    pass

class Waiter(Staff):
    pass

class Chef(Staff):
    pass

class Manager(Staff):
    pass


#testmenu = Menu()
#testmenu.add_item(MenuItem("banana", 1, "snack"))

#print(testmenu.foodItems[0])

#time.sleep(50)