# # multilevel inheritance
# class Animal:
#     def speak(self):
#         return "Animal speaks."
    
# class Dog(Animal):
#     def bark(self):
#         return "Dog barks."
    
# class Labrador(Dog):
#     def color(self):
#         return "Labrador is brown."
    
# my_labrador = Labrador()

# print(my_labrador.color())
# print(my_labrador.bark())
# print(my_labrador.speak())


#hierarchial
class Animal:
    def speak(self):
        return "Animal speaks."

class Dog(Animal):
        def bark(self):
            return "Dog barks."

class Cat(Animal):
     def meow(self):
          return "Cat meows."
     
my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())

print(my_dog.bark())
print(my_cat.meow())