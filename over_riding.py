class Animal:
    def sound(self):
        print("Some animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()       
