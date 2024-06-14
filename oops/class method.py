class Student:
    college='xyz'
    
    @classmethod
    def classMethod(cls):
        print(cls.college)
        del cls.college 
        print(cls.college)
        
Student.classMethod()
student1=Student()
student1.classMethod()
