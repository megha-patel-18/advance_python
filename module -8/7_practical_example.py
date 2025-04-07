#7) Write a Python program to handle exceptions in a calculator.

a=int(input("enter any number"))
b=int(input("enter any number "))


choice=int(input("enter a number between 1 to 4 :"))
print("1.addition")
print("2 . substraction ")
print("3. multiplication ")
print("4 . division ")


if choice==1:
    print ("addition ",a+b)

elif choice==2 :  
    print ("substraction ",a-b)

elif choice==3:
    print ("multiplication ", a*b)

elif choice==4 :
    print("division ",a%b)    

try:
    n = 0
    y = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", y)
    
finally:
    print("Execution complete.")