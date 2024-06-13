from abc import ABC,abstractmethod 
class A(ABC): 
    @abstractmethod
    def method1(self):
        pass 
    def method2(self):
        print("this is a concrete method")

    @abstractmethod 
    def method3(self):
        pass 
    
class B(A):
    def method1(self):
        print("method1 is implement is sub class")
    def method3(self):
        print("method3 is implemented3 in sub class")


obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()