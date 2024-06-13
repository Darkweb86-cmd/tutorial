class Human:
    def __init__(self,first,last,age):
        self.first=first 
        self.last=last 
        if age>=0:
            self._age=age
        else:
            self._age=0
    def getAge(self):
        return self._age
    def setAge(self,newAge):
        if newAge>=0:
            self._age=newAge
        else:
            self._age=0
            
a=Human("rohit","kumar",24)
print(a.getAge())
print(a.setAge(56))
print(a.getAge())