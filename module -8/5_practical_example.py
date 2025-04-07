 #5) Write a Python program to read a file and print the data on the console
file = open("i love python", "r")

# Read the entire content of the file
content = file.read()

print(content)

# Close the file
file.close()