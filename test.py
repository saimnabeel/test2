print(" ==========Welcome to the calculator==========")   
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("enter sign of operation (+, -, *, /): ")
try:
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    else:
        print("Invalid operation sign")
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
print("========Answer of the operation is: ", answer,"========")
print("============Thank you for using the calculator!============")           