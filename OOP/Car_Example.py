# class car():
#     def __init__(self, name, color, model):
#         self.Car_Name = name
#         self.Car_Color = color
#         self.Car_model = model


# x = car("Audi", "Green", 2022)
# print(x.Car_Name)


# Python program to create instance
# variables inside methods

class Car:
    # Class Variable
    vehicle = 'car'
    # The init method or constructor

    def __init__(self, model):
        # Instance Variable
        self.model = model
    # Adds an instance variable

    def setprice(self, price):
        self.price = price
    # Retrieves instance variable

    def getprice(self):
        return self.price


# Driver Code
Audi = Car("R8")
Audi.setprice(1000000)
print(Audi.getprice())
