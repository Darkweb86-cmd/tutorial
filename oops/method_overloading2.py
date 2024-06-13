class Parent1:
    def method(self):
        print("this is parent1 method")
        
class Parent2:
    def method(self):
        print("this is parent2 method")
        
class Child(Parent1,Parent2):
    pass
    # def method(self):
        # print("this is parent3 method")
        
obj=Child()
obj.method()
# class Student:
#     def __init__(self,name,rollno,address,phoneno):
#         self.name=name 
#         self.rollno=rollno 
#         self.address=address 
#         self.phoneno=phoneno 
# s1=Student("A",1,'a',23565)
# s2=Student("B",2,'b',45786)
# s3=Student("C",3,'c',78786)
# s4=Student("D",4,'d',78567)

# for obj in [s1,s2,s3,s4]:
#     print(obj.name)
#     print(obj.rollno)
#     print(obj.address)
#     print(obj.phoneno)

