class Book:
    def __init__(self, name, year):
        self.name = name
        self.year = year


b1 = Book("Geo", 2022)


class Newspaper:
    def __init__(self, name, year):
        self.name = name
        self.year = year


n1 = Newspaper("Ghang", 2022)


# print("++++++++++++++++++++++++++++\n")
# print(b1.name)
# print(n1.name)
# print("++++++++++++++++++++++++++++\n")


# print(type(b1))
# print(type(n1))

# print(type(b1) == type(b1))
# print(type(n1) == type(n1))
# print(type(b1) == type(n1))
# Built in isinstance method to check


# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(b1, object))
# print(isinstance(n1, object))
