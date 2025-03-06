
# classes and objects 
class Dog:
# A simple class attribute 
    atr1 = "Dog"
    atr2 = "Bark"
# A sample method/function   
    def fun(self):
        print("I'm a", self.atr1)
        print("I", self.atr2)
# Object instantiation  
Rodger = Dog()
# Accessing class attributes  
print(Rodger.atr1)
print(Rodger.atr2)
# and method through objects  s
Rodger.fun()
# --------LIBRARY EXAMPLE--------
print("This is the liabrary example")
# classes and objects
class library:
    book1 ="Python Rocks!"
    book2 ="Java Rocks!"
def fun(self):
    print("I first read",self.book1)
    print("I then read",self.book2)
university = library()
print(university.book1)
print (university.book2)