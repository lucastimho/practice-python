mylist = [1, 2, 3]


class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog(breed="Lab", name="Sammy", spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
