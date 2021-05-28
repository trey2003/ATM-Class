class Category:
    def __init__(self, food, clothing, car_expenses):
        self.food = food
        self.clothing = clothing
        self.car = car_expenses
        self.balance =  self.food + self.clothing + self.car
    def deposit(self, dep):
        self.balance = self.balance + dep
        return self.balance
    def withdraw(self, dep1):
        self.balance = self.balance - dep1
        return "Your current balance is " + str(self.balance)
    def transfer(self, self1, ammount):
        self.balance = self.balance - ammount
        self1.balance = self1.balance + ammount
        return "Your current balance for self is " + str(self.balance) + "\nYour current balance for self1 is " + str(self1.balance)
    def check_balance(self):
        print("Your current balance is " + str(self.balance))
        return self.balance
ctg = Category(100,300,500)
ctg1 = Category(1,1,1)
print(ctg.transfer(ctg1, 90))
