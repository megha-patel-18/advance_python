# 3) Write a Python program to create a file and write a string into it. 
with open("file.txt", "w") as f:
    f.write("Created using write mode.")

f = open("file.txt","r")
print(f.read())
