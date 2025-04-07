 #15) Write a Python program to show multiple inheritance.

class dog :
    def dogtype (self):
        print("this is labra dog !")

class dogage(dog):
    def doginfo(self):
        print(" labra dog live for 10 to 14 years.")


class  dogfood (dogage):
    def doginfo11(self):
        print("labra dog genrally eat pedigree ")   

self=dog()
self.dogtype()
self=dogage()
self.doginfo()
self=dogfood()
self.doginfo11()        
