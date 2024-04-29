# ABSTRACTION
# hiding the implementation details of a
#class and only showing the essential
#features to the user.


# class Car:
#     def __init__(self):
#         self.accr = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.accr = True
#         self.clutch = True
#         print("car started.....")
# c1 = Car()
# c1.start()


#ENCAPSULATION--------
#wrapping data and functions into a single unit(object)

####practice--

#create account class with 2 attributes - balance and account no.
#create methods for debit, credit and printing the balance.


class Account:
    def __init__(self, balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance -= amount
        print("RS.",amount,"total amount =",self.get_balance())


    def credit(self,amount):
        self.balance += amount
        print("RS.",amount,"total amount =",self.get_balance(),"was credited")

    def get_balance(self):
        return self.balance
acc = Account(15000,858548)
acc.debit(5000)
acc.credit(3000)

