class Animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def p_habtiat(self):
        print(self.habitat)
    def sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def __init__(self):
        super().__init__("bark")
    def sound(self):
        print("woof woof!")
q=Dog()
q.p_habtiat()
q.sound()
p=Animal()
p.sound()