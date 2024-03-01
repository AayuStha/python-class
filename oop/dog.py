class Dog:
    def __init__(self, name, age, random):
        self.name = name
        self.age = age
        self.random = random
        
    def bark(self):
        random = self.random + 5
        return f"Woof! - {random}"
    
class German(Dog):
    def __init__(self, name, age, random, food):
        super().__init__(name, age, random)
        self.food = food
        
    def eat(self):
        return f"{self.name} eats {self.food}"
    
my_dog = German("Buddy", 3, 2, "pedigree")


print("Name:", my_dog.name)
print("Age:", my_dog.age)

print("Bark:", my_dog.bark())

print(my_dog.eat())