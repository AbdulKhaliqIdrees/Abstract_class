#Concept of Interface
from abc import ABC,abstractmethod #importing ABC module
class Army(ABC): #abstract class
    def __init__(self,n): #Constructor
        self.number=n
    @abstractmethod #abstract method
    def disp(self):
        pass
    @abstractmethod #abstract method
    def show(self):
        pass
class Gun(Army): #Inherit Class From Abstract Class
    def disp(self): #Calling abstract method of abstract class
        print("Gun Number:",self.number)
        print("Gun:AK 47")
class Area(Gun): #Inherit From Normal Class
    def show(self):  #Calling abstract method of abstract class
        print("Area Number:",self.number)
        print("Lahore")

a=Area(187649) #Creating Object of Simple Class
a.disp() #Run Abstract Method with the help of Simple Class Object
print()
a.show() #Run Abstract Method with the help of Simple Class Object
