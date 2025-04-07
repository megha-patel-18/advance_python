# Write a Python program to create a class and access its properties using an object
class makeup:
    name = ""
    exdate = 0

makeup1 = makeup()

makeup1.exdate= 12
makeup1.name="blush"

print(f"Name: {makeup1.name}, exdate: {makeup1.exdate} ")