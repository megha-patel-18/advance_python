# Write Python programs to demonstrate method overloading and method overriding.
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

def product(a,b):
    
    p = a*b
    print(p)

def product(a,b,c):
    p=a*b*c
    print(p)


