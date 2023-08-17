class BankAccount:

    def __init__(self,initalBalance):
        self.__balance = initalBalance

    def menu(self):
        option = int(input("Enter the Option: "))
        if option == 1:
            self.deposit()
        elif option == 2:
            self.withDraw()
        elif option == 3:
            self.getBalance()

    def deposit(self):
        amount = int(input("Enter the Amount to Desposit"))

        if amount > 0:
            self.__balance += amount
        else:
            return "Balance Must be greater than 0"

    def withDraw(self):
        am = int(input("Enter the amount to withdraw: "))
        if am > 0 :
            self.__balance -= am

    def getBalance(self):
        return self.__balance

ali = BankAccount(2000)
print(ali.menu())
print(ali.getBalance())