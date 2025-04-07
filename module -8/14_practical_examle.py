# Write a Python program to show multilevel inheritance.

class employee :
     def empinfo(self):
          print( "he is a tech employee")


class employeedb(employee):
     def empinfo1(self) :
          print("his name is rahul ")    


class employeepersonalinfo(employee)    :
     def empinfo2(self)   :
          print("he is working with python to devlop website")     


self=employee()
self.empinfo()
self=employeedb()
self.empinfo1()
self=employeepersonalinfo()
self.empinfo2()