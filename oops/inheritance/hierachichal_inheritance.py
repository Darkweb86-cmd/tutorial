class Parent:
    def ParentMethod(self):
        print("i am a parent")
class Child1(Parent):
    def ChildMethod(self):
        print("I am a first child")
        
class Child2(Parent):
    def ChildMethod(self):
        print("i am a second child")

child1=Child1()
child1.ChildMethod()
child1.ParentMethod()
child2=Child2()
child2.ChildMethod()
child2.ParentMethod()