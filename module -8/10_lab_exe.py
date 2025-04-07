# Write Python programs to demonstrate different types of inheritance (single, multiple,multi level)


class Parent:
    def func1(self):
        print("This function is in parent class.")
 
 
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
 

object = Child()
object.func1()
object.func2()



class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 

 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 

 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 

s1 = Son()
s1.fathername = "jayeshbhai"
s1.mothername = "neetaben"
s1.parents()




 
 
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        
        Grandfather.__init__(self, grandfathername)
 

 
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
 

s1 = Son('ronak', 'jayeshbhai', 'ravjibhai')
print(s1.grandfathername)
s1.print_name()

