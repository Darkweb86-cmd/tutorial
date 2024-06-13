# the __init__() method 
# classes python can have a special __init__() method which gets called everytime you create an instance of the class(instantiate)
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        print("i am run init")
    def display(self):
        print("i am in details")
        return f"his name is {self.name}. He is {self.age} years old."
# instancing a class
p1=Person("rohit",23)
p2=Person("prasad",35)
# here,p1 and p2 are the instance of person class.
# we can build any number of object using the same class blueprint 
print(p1.display())
