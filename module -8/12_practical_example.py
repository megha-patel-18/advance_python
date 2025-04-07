# Write a Python program to demonstrate the use of local and 
#global variables in a class.


#global variable :
def f():
    global s
    s += ' GFG'
    print(s)
    s = " python is easy to learn language"
    print(s) 

s = "Python is great!" 
f()
print(s)

#local variable :
def f():

    
    s = "I love Geeksforgeeks"
    print(s)


f()