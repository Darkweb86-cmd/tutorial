class BankAccount:
    def __init__(this,accountno,accountName,ifsccode,balance):
        this.accountno=accountno
        this.accountName=accountName
        this.ifsccode=ifsccode 
        this.balance=balance 
    def withdraw(this,amount):
        this.balance-=amount    
    def deposit(this,amount):
        this.balance+=amount
    def checkbalance(this):
        print(this.balance)
        
object1=BankAccount(1235654,"jia","BYXPA3569G",10000)
object2=BankAccount(1235654,"kia","BYXPA3569G",10000)
print(object1.accountName)
print(object2.accountno)
object1.checkbalance()
object1.deposit(500)
object1.withdraw(200)
object1.checkbalance()
