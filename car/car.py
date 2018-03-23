class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        self.tax_calc()
    def tax_calc(self):
        if self.price >  10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price: ", self.price
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: ", self.tax
        print ""

car1 = Car(10000, "130mph", "Full", "20mpg")
car1.display_all()

car2 = Car(7000, "90mph", "Half Full", "35mpg")
car2.display_all()

car3 = Car(15000, "140mph", "Empty", "20mpg")
car3.display_all()

car4 = Car(9000, "85mph", "3/4 Full", "45mpg")
car4.display_all()

car5 = Car(11000, "100mph", "1/4 Full", "30mpg")
car5.display_all()

car6 = Car(3000, "80mph", "Empty", "20mpg")
car6.display_all()