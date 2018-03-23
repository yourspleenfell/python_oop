class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self   
class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Dog", 150)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("Dragon", 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

panda = Animal("Panda", 100).walk().walk().walk().run().run().display_health()

dog = Dog().walk().walk().walk().run().run().pet().display_health()

drogo = Dragon().walk().walk().run().run().fly().display_health()

cat = Animal("Cat", 70).walk().walk().walk().run().run().display_health()