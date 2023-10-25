#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

temp = input("Enter a Temperature you like to Convert:" )
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5/9))
    o_convention = "Celsius"
else:
    print("Input Proper Convention")
    
print("The Temperature in", o_convention, "is", result, "degrees.")