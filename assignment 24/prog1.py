class data():
    def __init__(self):
        
      self.name=input("enter your name:")
class data2():
    def __init__(self):
     self.age=int(input("enter age:"))
class data3(): 
   def __init__(self):
     self.email=eval(input("enter email:"))
s1=data()
s2=data2()
s3=data3()
print(s1.name())
print(s2.age())
print(s3.email())
'''class student:
    
     school="ineuron" # school is variable of class
    
     def __init__(self):
         self.marks=10
         
     def get_marks(self): # instance methods (self pass hota he)
        return self.marks
     @classmethod
     def get_school(cls):    #class method
      return cls.school 
     
     @staticmethod
     def add(x,y): # x and y are       """static method"""
         return x+y
     
        
s1=student()
s2=student()
print(s1.marks)         
print(s2.school)
print(s1.get_school())
print(s1.add(2,5))
 '''
    