# class Employee:
#     def instanceMethod(self):
#         print("instance method created")
#     def instanceMethod2(self,a,b):
#         print(a,b)

# # How to call an instance method 
# # syntax: object.intanceMethod(parameters)

# emp1=Employee() 
# #emp1-->def instanceMethod1(self):
# emp1.instanceMethod()

class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name 
        self.emp_id=emp_id 
        self.salary=salary 
    def getEmployeeName(self):
        print(self.name)
emp1=Employee('pavan',1000100,40000)
# init method calls when we create an object to employee class
print(emp1.name)         
print(emp1.emp_id)         
print(emp1.salary)         

# self.variable =value 
# self.variable is an instance variable
# how to access variables in instance method 
# self.variableName 
emp1.getEmployeeName()
emp2=Employee('ravi',299910,3000)
emp2.getEmployeeName()
# we can access class variables and instance variables using object 
# to access class variable self.classVariable 
