# program to calculate 2 numbers
# made by itsmeevil

print("***A Simple Calculator***\n\nCalculator to calculate 2 numbers\nOptions:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (x)\n4. Division (÷)\nNote - You can only choose 1 out of the 4 options\n")

num1 = float(input("Enter the first number: "))
arithmetic = input("Enter the option (1/2/3/4): ")
num2 = float(input("Enter the second number: "))

if arithmetic == "1":
	res = num1 + num2

	print(f"\nCalculation:\n{num1} + {num2} = {res}")
	print(f"\nResult:\nThe sum of {num1} and {num2} is {res}")
elif arithmetic == "2":
	res = num1 - num2

	print(f"\nCalculation:\n{num1} - {num2} = {res}")
	print(f"\nResult:\nThe subtraction of {num1} and {num2} is {res}")
elif arithmetic == "3":
	res = num1 * num2

	print(f"\nCalculation:\n{num1} × {num2} = {res}")
	print(f"\nResult:\nThe multiplication of {num1} and {num2} is {res}")
elif arithmetic == "4":
	res = num1 / num2

	print(f"\nCalculation:\n{num1} ÷ {num2} = {res}")
	print(f"\nResult:\nThe division of {num1} and {num2} is {res}")
else:
	print("\nERROR:\nEnter the correct arithmetic (1/2/3/4)!")
