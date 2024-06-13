# what is class?
# a class is a blueprint for the object 
# we can think of parrot with labels. it contains all the details about the name,color,size etc. 
# based on these descriptions ,we can study about the parrot here a parrot is an object 
# eg: class Parrot:
 # pass
# here, we use the class keyword to define an empty class 'parrot' from class, we construct instance ,an instance is a specific object created 
# from a particular class 
# what is an object?
# an object is an instantiation of a class .when class is defined only the description for the object is defined . Therefore ,
# no memory or storage is allocated 
# eg: obj=Parrot()
# here,obj is an object reference of class parrot 

class Parrot:
    pass 
obj=Parrot()
print(obj)
