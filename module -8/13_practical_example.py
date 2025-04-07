#13) Write a Python program to show single inheritance. 

class student :
    def studentinfo(self) :
        print("hello ! i m megha my roll no is 21 .")

class studentdb(student) :
    def studentinfo2(self):
        print("i am a tech student")    

self=studentdb()
self.studentinfo()  
self.studentinfo2()     
