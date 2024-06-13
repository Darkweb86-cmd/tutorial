class Animal:
    def __init__(self,name,special):
        self.name=name 
        self.special=special 
        
    def __repr__(self):
        return f"{self.name} is a {self.special}"
    
    def make_sound(self,sound):
        print(f"this animal say {self.sound}")
        
class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,special='cat') # write using super() method self is not necessary 
        self.breed=breed 
        self.toy=toy 
    def play(self):
        print(f"{self.name} is playing with {self.toy}")
        
c=Cat("helcat","scottish","yes")
print(c.play())
print(c.special)