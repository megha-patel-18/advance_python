#11) Write a Python program to create a class and access the properties 
#of the class using an object.
class employee:
    info = "megha"

    def __init__(self, name, age):
        self.name = name  
        self.age = age

emp1 = employee("reetu", 21)

print(emp1.name) 
print(emp1.info) 