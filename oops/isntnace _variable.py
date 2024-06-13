class A:
    staticVariable1=10 
    staticVariable2=20 
    
    def sampleMethod(self):
        print('sample method')
    
A.staticVariable3=30
print(A.staticVariable1)
print(A.staticVariable2)
print(A.staticVariable3)