# Define a Class
class Book:
    def __init__(self, title, pages, price) -> None:
        self.title = title
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

        # if hasattr(self, "_coupon"):
        #     return self.prince - (self.prince * self.discount)

    def discount(self, amount):
        self._discount = amount

    # def coupon(self, coupon):
    #     self._coupon = coupon


        # Create an object for your book class
b1 = Book("Harry Potter", 1250, 2500)
# print(b1)
# print(b1.title)
# print(b1.pages)
# print(b1.price)
print(b1.getprice())
b1.discount(0.50)
print(b1.getprice())
# b1.coupon("Ali")
