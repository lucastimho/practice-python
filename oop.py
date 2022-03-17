mylist = [1, 2, 3]


class Dog():
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, age):
        print("Woof! My name is {} and I am {} years old.".format(self.name, age))


my_dog = Dog("lab", "Sammy")
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
my_dog.bark(3)
