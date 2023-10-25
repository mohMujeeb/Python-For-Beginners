"""
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

number = 5

for i in range(number):
    for j in range(i):
        print("* ", end="")
    print(" ")
    
for i in range(number, 0, -1):
    for j in range(i):
        print("* ", end= "")
    print(" ")