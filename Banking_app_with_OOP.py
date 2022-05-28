# Banking App

# 1 --> Parent Class: User
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # function to show user details.
    def show_details(self):
        print('Personal Details:')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)
# nathan = User('Nathan', 21, 'male')
# nathan.show_details()

# 2 --> Child Class of User class
class Bank(User):
    def __init__(self, name, age, gender):
        # to inherit all init method arg from super class 'User', we call the super() function
        super().__init__(name, age, gender)
        # sort details for balance.
        self.balance = 0

    # an instance method to sort user deposits.
    def deposit(self, amount):
        # updating user balance with new deposits.
        self.balance = self.balance + amount
        print(f'Hello {self.name}, your Account balance has been updated: ${self.balance}')

    # method to withdraw
    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print(f'sorry, {self.name}, you have insufficient balance of ${self.balance}... ')
        else:
            self.balance = self.balance - withdraw_amount
            print(f'Hello {self.name} withdraw of ${withdraw_amount} successful, new balance is: ${self.balance}')

    # method to view balance.
    def view_balance(self):
        self.show_details()
        print(f'Hello {self.name}, available balance is {self.balance}')

# nathan = Bank('Nathan', 21, 'male')
# nathan.deposit(200)
# nathan.deposit(200)
# nathan.withdraw(350)
# nathan.withdraw(350)
# nathan.withdraw(30)
# nathan.view_balance()