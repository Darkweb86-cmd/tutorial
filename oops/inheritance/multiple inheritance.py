class Father:
    def method1(self):
        print('i am a father')
class Mother:
    def method2(self):
        print("i am a mother")
        
class Child(Father,Mother):
    def method3(self):
        print('i am child')
        
child1=Child()
child1.method3()
child1.method2()
child1.method1()
print(Child.__mro__)