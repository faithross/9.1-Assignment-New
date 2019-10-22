#myParentClass
class BankAcount():
    def __init__(self, accountNumber, balance):
        self.balance = balance
        self.accountNumber = accountNumber # MM - I added this value. I realized I made a hasty mistake earlier

    def deposit(self): # MM - I added amount here
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
       
    def withdraw(self): # MM - I added amount here
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)
   
# creating an object of class
s = BankAcount("acct12345", 250.00) # this needs to have values for balance and fees

# Calling functions with that class object
s.deposit() # MM this requires the amount to deposit
s.withdraw() # MM this requires the amount to withdraw
s.display()  # MM this is fine

'''
    # MM This code is not needed.

    def getBankAcount(self, balance):
        return balance.fees + "" + balance.interestrate + " has " + str(minimumbalance)
'''

#my 1st Child class
class CheckingAccount(BankAcount):
    def __init__(self, accountNumber, balance, fees, minimumbalance): # I removed interestRate, it belogs with SavingsAccount.
        BankAcount.__init__(self, accountNumber, balance) # Needs only accountNumber and balance
        #self.balance = balance # this is part of parent class and is set in the above line
        self.fees = fees
        self.minimumbalance = minimumbalance

    def deductFees(self): # MM missing 'self'
        amount = float(input("Enter amount of fees: ")) # you were missing variable
        self.balance += amount
        print("\n Amount Fees:", amount)

    # ------ start below here -------
    def checkMinimumBalance():
        try:
           amount = float(input("Enter Minimum Balance amount : "))
           self.balance >= amount
           self.balance -= amount
        except:
            print("error in bank account class")
            balance=int(input("Enter you balance"))
        if(balance<50):
            obj1= MinimumBalance()
            print(obj1.message)
        else:
            obj2= BankAccount(balance)

    def getSavingAccount(balance):
        return balance.getFees() + "And it has" + str(minimumbalance) + "minimum balance."


#my2ndchildclass
class SavingAccount(BankAcount):
    def __init__(self, accountNumber, balance, interestrate): # parent variables and SavingsAccount variables shoudl go here
        Balance.__init__(self, accountNumber, balance, interestrate) # this should inherit from the parent class, not Balance
        self.balance = balance # this is not required here
        self.interestrate = interestrate
        
    def addInterestrate(self):
        amount = float(input("Enter amount of interest: "))
        self.balance += amount
        print("\n Amount interst:", amount)
        
'''
    # MM This code is not needed.     
    def getSavingAccount(balance):
        return balance.interestrate + "And it has" + balance.interestrate + " has " + str(minimumbalance)
'''
