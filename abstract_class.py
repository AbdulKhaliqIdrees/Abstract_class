#Learn Concept of Abstract Class
from abc import ABC,abstractmethod #importing abc Module
class TenGreen(ABC): #Abstract Class
    def __init__(self,n): #Constructor
        self.RollNo=n
    @abstractmethod
    def name(self):  #Abstract Method
        pass
    @abstractmethod
    def position(self): #Abstract Method
        pass
    def comments(self): #Concrete Method
        print("This Student Passed the Exams with Good Grades")
class First(TenGreen): #Inherit From Abstract Class
    def name(self): #Calling Abstract Method of Base Class
        print("Topper Name::Ali Ahmad") 
        print("RollNo:",self.RollNo)
    def position(self): #Calling Abstract Method of Base Class
        print("Ali Got First Position")
class Second(TenGreen): #Inherit From Abstract Class
    def name(self): #Calling Abstract Method of Base Class
        print("Topper Name::Hamza")
        print("RollNo:",self.RollNo) 
    def position(self): #Calling Abstract Method of Base Class
        print("Hamza Got Second Position") 
class Third(TenGreen): #Inherit From Abstract Class
    def name(self): #Calling Abstract Method of Base Class
        print("Topper Name::Rayan") 
        print("RollNo:",self.RollNo)
    def position(self): #Calling Abstract Method of Base Class
        print("Rayan Got Third Position")   

f=First(45) #Creating Object of First Class
f.name()  #Calling abstract Method with First Class Object
f.position() #Calling abstract Method with First Class Object
f.comments() #Calling concrete Method with First Class Object
print()
s=Second(34) #Creating Object of Second Class
s.name()   #Calling abstract Method with First Class Object
s.position() #Calling abstract Method with First Class Object
s.comments() #Calling concrete Method with First Class Object
print()
t=Third(77)  #Creating Object of Third Class
t.name()    #Calling abstract Method with First Class Object
t.position() #Calling abstract Method with First Class Object
t.comments()  #Calling concrete Method with First Class Object
