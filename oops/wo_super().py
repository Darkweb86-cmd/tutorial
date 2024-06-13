# super() function 
# the super() built returns a proxy object(temporary object of the superclass) that allows us to access methods of the base class 
# in python, super() has two major use cases:
# allows us to avoid using the base class name explicity 
# working with multiple inheritance 

 
class Animal:
    def __init__(self,name,special):
        self.name=name
        self.special=special
    def __repr__(self):
        return f"{self.name} is a {self.special}" 
    def make_sound(self,sound):
        print(f" this animal says {self.sound}")
class Cat(Animal):
    def __init__(self,name,special,breed,toy):
        Animal.__init__(self,name,special) # without super keyword
        self.breed=breed
        self.toy=toy 
c=Cat("Hellcat","cat","scottish","yes")
print(c)
print(c.special)
print(c.breed)
print(c.toy)