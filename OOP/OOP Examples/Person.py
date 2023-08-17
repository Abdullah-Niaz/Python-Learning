class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Public method to access the private name

    def get_age(self):
        return self.__age   # Public method to access the private age


# Creating an instance of the Person class
Ali = Person("Ali", 30)

# Getting personal information using the public methods
print("Name:",Ali.get_name())
print("Age:",Ali.get_age())
