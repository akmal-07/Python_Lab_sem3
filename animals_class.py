class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"{self.name} barks : woof! woof!")
class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    def meow(self):
        print(f"{self.name} meows: Meow Meow!!")
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    def fly(self):
        print(f"{self.name} is flying .")
dog = Dog("Tommy", "Labrador")
cat = Cat("Kitty", "White")
bird = Bird("Tweety", "Sparrow")
dog.eat()
dog.bark()
dog.sleep()

cat.eat()
cat.meow()
cat.sleep()

bird.eat()
bird.fly()
bird.sleep()
