 # inheritance (parent-child)
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):  # Inheriting Animal
    def bark(self):
        print("Dog barking")

d = Dog()
d.speak()  # Animal speaking
d.bark()   # Dog barking
    