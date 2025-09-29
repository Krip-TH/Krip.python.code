"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""

class Animal:
    def move(self):
        print("Animal moves")

class Fish(Animal):
    def move(self):
        print("Fish swims")

class Bird(Animal):
    def move(self):
        print("Bird flies")

class Dog(Animal):
    def move(self):
        print("Dog runs")

def animal_move(animal):
    animal.move()

for animal in [Fish(), Bird(), Dog()]:
    animal_move(animal)
