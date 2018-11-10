
class Dog:
    def __init__(self):
        self.name = 'test'
        self.friends = [["Remo",10],["Ray",20]]

        def agefinder(self):
            for friend in self.friends:
                print(friend)

class BankAccount:
    #### NO CLASS VARIABLES
    def __init__(self):
        self.balance = 500 #This is an instance variable

    def set_account_type(self,actype):
        self.type=actype
    
    def withdraw(self, amount): 
        self.balance = self.balance - amount
        print("You withdrew {} dollars\n".format(amount))
        return self.balance

    def deposit(self, amount): 
        self.balance += amount
        print("You deposited {} dollars\n".format(amount))
        return self.balance
      
    def printbal(self):
        print("Your balance is currently {} dollars".format(self.balance))
        return self.balance

class User:
    def __init__(self):
        self.checkingaccount = BankAccount()
        self.savingsaccount = BankAccount()
        self.checkingaccount.set_account_type("checking")
        self.savingsaccount.set_account_type("checking")

    def deposit(self, amount):
        self.checkingaccount.deposit(amount)
        self.savingsaccount.deposit(amount)
    
    def printbal(self):
        self.checkingaccount.printbal()
        self.savingsaccount.printbal()

    def transfer(self, amount):
        while True:
            try:
                userinput=input('Enter from account : 1.Checking 2.Savings\n')
                answer=int(userinput)
                break
            except ValueError:
                print('invalid entry')
            except KeyboardInterrupt:
                print('bad value')            

        if answer == 1:
            print("you entered ",answer)
            self.checkingaccount.withdraw(amount)
            self.savingsaccount.deposit(amount)
        else:
            print("invalid")    

user = User()
user.printbal()
user.deposit(200)
user.printbal()
user.transfer(50)
user.printbal()
