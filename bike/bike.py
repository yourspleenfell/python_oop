class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        print "...Riding..."
        self.miles += 10
    def reverse(self):
        if self.miles > 0:
            print "...Reversing..."
            self.miles -= 5
        else:
            print "0 miles, cannot be reversed"
    def displayinfo(self):
        print "Price: ", self.price
        print "tota Miles: ", self.miles


bike1 = Bike(399.99, "30mp/h")
bike2 = Bike(599.99, "40mp/h")
bike3 = Bike(799.99, "45mp/h")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()