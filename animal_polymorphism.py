# Base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses with their own implementation of move()
class Dog(Animal):
    def move(self):
        return "The dog runs on four legs."

class Bird(Animal):
    def move(self):
        return "The Eagle flies through the sky."

class Fish(Animal):
    def move(self):
        return "The Tilapia swims in the water."

class Snake(Animal):
    def move(self):
        return "The Cobra slithers silently."

# Function that takes any Animal and calls its move() method
def show_animal_movement(animal):
    print(animal.move())

# Example usage
animals = [Dog(), Bird(), Fish(), Snake()]

for animal in animals:
    show_animal_movement(animal)
