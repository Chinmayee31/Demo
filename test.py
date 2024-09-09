# Define a class named `Animal`
class Animal:
    def __init__(self, name, species):
        self.name = name       # Instance variable for the name of the animal
        self.species = species # Instance variable for the species of the animal

    # Method to make the animal speak
    def speak(self):
        return f"{self.name} makes a sound."

# Define a subclass named `Dog` that inherits from `Animal`
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog") # Initialize the parent class with species as 'Dog'
        self.breed = breed                    # Instance variable for the breed of the dog

    # Method to make the dog speak
    def speak(self):
        return f"{self.name} barks."

# Define another subclass named `Cat` that inherits from `Animal`
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat") # Initialize the parent class with species as 'Cat'
        self.color = color                    # Instance variable for the color of the cat

    # Method to make the cat speak
    def speak(self):
        return f"{self.name} meows."

# Function to display information about an animal
def describe_animal(animal):
    print(f"Name: {animal.name}")
    print(f"Species: {animal.species}")
    print(f"Sound: {animal.speak()}")

# Creating instances of Dog and Cat
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Gray")

# Using the function to describe the animals
describe_animal(dog)
describe_animal(cat)
