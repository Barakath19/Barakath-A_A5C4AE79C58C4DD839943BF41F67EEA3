class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        return self.__account_balance

# Testing the BankAccount class
account = BankAccount("123456789", "John Doe")
account.deposit(1000)
account.withdraw(500)
print(account.display_balance())