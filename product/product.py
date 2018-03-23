class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.tax = 0
        self.total = 0
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.returned =  ""

    def sell(self):
        self.price = 0
        self.total = 0
        self.tax = 0        
        self.status = "sold"
        return self

    def add_tax(self, float):
        self.tax = float
        self.total = float + self.price
        return self.total

    def return_prod(self, reason):
        if reason == "defective":
            self.price = 0
            self.total = 0
            self.tax = 0
            self.status = "defective"
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "used"
            self.price = self.price - (self.price*0.2)
        return self

    def display_info(self):
        print "Item Name: " + self.item_name
        print "Brand: " + self.brand
        print "Item Price:", self.price
        print "Product Tax:", self.tax
        print "Total Price:", self.total
        print "Weight: " + self.weight
        print "Status: " + self.status
        print ""
        return self

prod1 = Product(5, "Room Spray", "0.1 lbs", "Febreeze")
prod1.return_prod("open box").add_tax(0.15)
prod1.display_info()

prod2 = Product(7, "Big Trash Bags", "0.2lbs", "Hefty")
prod2.add_tax(0.09)
prod2.return_prod("defective").display_info()

prod3 = Product(15, "Wax Melter", "0.4 lbs", "Scentsy")
prod3.add_tax(0.13)
prod3.sell().display_info().return_prod("in box").display_info()