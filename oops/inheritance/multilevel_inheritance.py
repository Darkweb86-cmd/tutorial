class GrandParent:
    def method1(self):
        print('i am a grand parent')
class Parent(GrandParent):
    def method2(self):
        print("i am a grand parent")
class Child(Parent):
    def method3(self):
        print("i am a grand child")
        
child1=Child()
child1.method1()
child1.method2()
child1.method3()
print(Child.__mro__)