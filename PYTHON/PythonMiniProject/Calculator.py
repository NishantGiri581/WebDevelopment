# Build a simple command-line calculator that perform basic arithmetic task

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error: Division by Zero"
    return x/y
print("===Simple Calculator===")
print("Choose Operation")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

op = input("Enter the Operation (+, -, *, /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if op == "+":
    result = add(a,b)
elif op == "-":
    result = subtract(a,b)
elif op == "*":
    result = multiply(a,b)
elif op == "/":
    result = divide(a,b)
else:
    result = "Invalid operator"    
print("Result: ", result)    