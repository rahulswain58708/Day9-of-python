class Animal:
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
d=Dog()
d.speak()  # Dog bark