class Animal():
    def __init__(self):
        print("Animal created.")

    def who_i_am(self):
        print("I am an animal.")

    def eat(self):
        print("I am eating.")


# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created.")

#     def who_i_am(self):
#         print("I am a dog.")

#     def bark(self):
#         print("WOOF!")


# my_dog = Dog()
# print(my_dog)

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof."


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow."


niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(felix)
