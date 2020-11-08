class Table():
    """a table at a restaurant"""
    water = {"Mineral water" : .5 , "Sparkl water" : 1.5}
    refreshments = {"Coca cola" : 2.5 , "Fanta" : 2.2 , "Sprite" : 1.9 , "Schweppes" : 2.6}
    beer = {"Heineken" : 2.2 , "Eza"  : 2.4 , "Amstel" : 2.3}
    menu = {**water , **refreshments , **beer}
    
    def __init__(self, num):
        self.num = num
        self.account = 0
        self.dishes = {}
        #Status: Empty, Reserved, InUse
        self.status = "Empty"
        
    def add_dish(self, item, quantity):
        if self.status == "Empty": self.set_status("InUse")
        if item in self.dishes.keys():
            self.dishes[item]+=quantity
            self.account+= (self.menu.get(item) * quantity)
        else:
            self.dishes[item]= quantity
            self.account+= (self.menu.get(item) * quantity)
            
    def remove_dish(self, item, quantity):
        if item not in self.dishes.keys():
            return False
        else:
            if quantity > self.dishes[item]: return False
            else:
                self.dishes[item] -= quantity
                self.account -= (quantity * self.menu.get(item))
    
    def get_dishes(self):
        return self.dishes
    
    def get_account(self):
        return self.account

    def get_id(self):
        return self.num

    def set_status(self, status):
        self.status = status
        
    def __str__(self):
        if self.status != "Empty": 
            return "Table's id:"+str(self.num)+"\nStatus:"+self.status+"\nCurrent account:"+str(self.account)+"\n"+str(self.dishes)
        else:
            return "Table's id:"+str(self.num)+"\nStatus:Empty"


class Restaurant():
    """Our model's restaurant"""
    def __init__(self):
        self.number_of_tables = self.numberOfTables()
        self.tables = []
        for i in range(self.number_of_tables):
            self.tables.append(Table(i+1))

    def numberOfTables(self):
        return int(input("Give the number of restaurant's tables"))

    def get_restaurant_status(self):
        for i in self.tables:
            print(i)
            print("************************************************")

if __name__ =='__main__':
    r = Restaurant()
    r.get_restaurant_status()







    
    
