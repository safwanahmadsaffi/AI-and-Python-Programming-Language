import os

class Employee:
    def __init__(self, name, salary,age):
        self.name = name
        self.salary = salary
        self.age =age

    def display(self):
        print('Name:', self.name, 'Salary:', self.salary,'Age :', self.age)

    def __del__(self):
        print('Deleted:', self.name)
        
object1 = Employee('safwan', 10000,22)
object2 =Employee('umer', 10000,20)
object2.display()
object1.display()
# Delete the object1
del object2
os._exit(0)