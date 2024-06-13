class GrandParent:
    def method(self):
        print("this is grandparent class ")
class Parent:
    def method(self):
        print('this is parent method')
class Child:
    def method(self):
        print("this is child method")
        
        
object1=Child()
object1.method()
parent1=Parent()
parent1.method()
