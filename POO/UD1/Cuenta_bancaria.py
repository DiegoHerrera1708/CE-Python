class backAccount:
    def __init__(self):
        pass

    def set_details(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def display(self):
        print("Account Holder:" , self.name)
        print("Account Balance:" , self.balance)

    def recall(self, amount):
        self.balance -=  amount
    
    def deposit(self, amount):
        self.balance += amount
    

obj1 = backAccount()
obj2 = backAccount()

obj1.set_details("David", 5000)
obj2.set_details("John")
obj1.display()
obj2.display()
obj1.recall(2000)
obj2.deposit(5000)
obj1.display()
obj2.display()
