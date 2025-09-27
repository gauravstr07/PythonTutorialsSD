class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def widthrew(self, amount):
        if amount > self.__balance:
            print("Insufficiant Funds")
        else:
            self.__balance -= amount
        return self.__balance
    
    def deposit(self, amount):
        limit = 1000
        if amount >= limit:
            print("you can not deposit more then", {limit})
        else:
            self.__balance += amount
            return self.__balance
        
    def showAmount(self):
        return self.__balance



account = BankAccount(120410, 500)

enterAmount = int(input("enter a amount - "))

account.deposit(enterAmount)

print("Total balance is - ", account.showAmount())