class BankAccount:
    def __init__(self,accountno,accountName,ifsccode,balance):
        self.accountno=accountno
        self.accountName=accountName 
        self.ifsccode=ifsccode 
        self.balance=balance 
    def display(self):
        print(self.accountno,self.accountName,self.ifsccode,self.balance)

object1=BankAccount(1235654,"jia","BYXPA3569G",10000)
object1.display()