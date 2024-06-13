# class Parent:
#     publicdata=10 
#     def publicMethod(self):
#         print(self.publicdata)
        
# class Child(Parent):
#     def method(self):
#         print(self.publicdata)
        
# obj1=Parent()
# obj1.publicMethod()
# print(obj1.publicdata)
# obj2=Child()
# obj2.method()
# print(obj2.publicdata)

# class Parent:
#     _protecteddata=10 
#     def publicmethod(self):
#         print(self._protecteddata)
# class Child(Parent):
#     def method(self):
#         print(self._protecteddata)
        
        
# obj1=Parent()
# obj1.publicethod()
# obj2=Child()
# obj2.method()
# print(obj1._protecteddata)

# class Parent:
#     __privateData=10 
#     def publicmethod(self):
#         print(self.__privateData)
# class Child(Parent):
#     def method(self):
#         print(self._Parent__privateData)
# obj1=Parent()
# obj1.publicmethod()
# obj2=Child()
# obj2.method()

class Bank:
        __balance=10000
        def getBalance(self):
            return self.__balance 
class API(Bank):
    def printBalance(self):
        return self.__balance
    
obj=API()
obj2=Bank()
print(obj.__balance)
print(obj2.__balance)

