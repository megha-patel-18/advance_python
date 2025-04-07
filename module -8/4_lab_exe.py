# Write a Python program to open a file in write mode, write some text, and then close it. 
file1 = open("Employees.txt", "w") 
lst = [] 
for i in range(3): 
    name = input("Enter the name of the employee: ") 
    lst.append(name + '\n') 
    
file1.writelines(lst) 
file1.close() 
print("Data is written into the file.") 