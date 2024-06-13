# what is an attribute?
# an attribute is a variable that holds data for an object
# what is a method?
# a method is a behaviour of an action of an object 
class Person:
    # class name should always starts with upper case 
    # you can put any variable in place of self 
    def sayName(self,name):
        self.personName=name 
        return f"my name is {self.personName}"
p=Person()
print(p.sayName('rohit'))