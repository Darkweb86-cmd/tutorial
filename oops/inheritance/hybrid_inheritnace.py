class GrandParent:
    def method1(self):
        print("I am grand parent")
class Parent1(GrandParent):
    def method2(self):
        print("i am a parent")

class Parent2:
    def method3(self):
        print("i am a parent2")

class Child(Parent1,Parent2):
    def method4(self):
        print("i am child")
        
        
child1=Child()
child1.method4()
child1.method3()
child1.method2()
child1.method1()