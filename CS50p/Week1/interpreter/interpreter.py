# Get input
math = input("Expression: ")
# Variables
x, y, z = math.split(" ")
# Change variables (x and z) to float
new_x = float(x)
new_z = float(z)

if y == "+":
    print(new_x + new_z)
elif y == "-":
    print(new_x - new_z)
elif y == "*" or y == "x":
    print(new_x * new_z)
elif y == "/":
# There should be a clarification about being unable to divide by zero
    if new_z !=0:
        m=new_x/new_z
        print(round(m, 1))
# Also missing an 'invalid input' response when the user doesn't write a correct caracter