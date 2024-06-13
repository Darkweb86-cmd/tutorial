class Human:
    def __init__(self,name,last,age):
        self.name=name
        self.last=last
        self.age=age
        if age>=0:
            self._age=age
        else:
            self._age=0
    @property # getter attribute 
    def age(self):
        return self._age 
    @age.setter #setter attribute 
    def age(self,newAge):
        if newAge>=0:
            self._age=newAge
        else:
            raise ValueError("Age cannot be negative")
a=Human("rohit","kumar",30)
print(a.age)
print(a.age==78)