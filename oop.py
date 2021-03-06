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


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return 2 * self.pi * self.radius


my_circle = Circle(30)
print(my_circle.radius)
