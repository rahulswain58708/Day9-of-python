#Polymorphism (Same function, different behavior)
class Cat:
    def speak(self):
        print("meow")

class Dog:
    def speak(self):
        print("bark")

def animal_sound(animal):
    animal.speak()
d= Dog()
c= Cat()
animal_sound(d)  #bark
animal_sound(c)  #meow