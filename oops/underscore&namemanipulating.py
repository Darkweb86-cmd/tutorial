class Person:
    def __init__(self):
        self.name="rohit" # public
        self._age=35  # private
        self.__height=6 # specific to class 
        
p=Person()
print(p.name)
print(p._age)
print(p._Person__height)# name 
p.name="prashanth ambala"
p._age=30
p._Person__height=7 
