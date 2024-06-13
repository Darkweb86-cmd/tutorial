class Parent:
    def method1(self):
        print("i am parent")
# create childClassName(parentclassName):
class Child(Parent):
    def method2(self):
        print("i am a child")

child1=Child()
child1.method2()
child1.method1()
parent1=Parent()
parent1.method2() # didn't get child symptoms to parent it will give error 
