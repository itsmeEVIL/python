# program to calculate 2 numbers
# made by itsmeevil

# print the available options
print("***A Simple Calculator***\n\nCalculator to calculate 2 numbers\nOptions:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (x)\n4. Division (÷)\nNote - You can only choose 1 out of the 4 options\n")

# input 1st num
num1 = float(input("Enter the first number: "))
# input option choosen
arithmetic = input("Enter the option (1/2/3/4): ")
# input 2nd num
num2 = float(input("Enter the second number: "))

# check the option you've entered
# if you choose 1st option - addition
if arithmetic == "1":
	# calculate the result
	res = num1 + num2
	# print calculation and result
	print("\nCalculation:\n", num1, "+", num2, "=", res)
	print("\nResult:\nThe sum of", num1, "and", num2, "is", res)

# if you choose 2nd option - subtraction
elif arithmetic == "2":
	# calculate the result
	res = num1 - num2
	# print calculation and result
	print("\nCalculation:\n", num1, "-", num2, "=", res)
	print("\nResult:\nThe subtraction of", num1, "and", num2, "is", res)

# if you choose 3rd option - multiplication
elif arithmetic == "3":
	# calculate the result
	res = num1 * num2
	# print calculation and result
	print("\nCalculation:\n", num1, "x", num2, "=", res)
	print("\nResult:\nThe multiplication of", num1, "and", num2, "is", res)

# if you choose 4th option - division
elif arithmetic == "4":
	# calculate the result
	res = num1 / num2
	# print calculation and result
	print("\nCalculation:\n", num1, "÷", num2, "=", res)
	print("\nResult:\nThe division of", num1, "and", num2, "is", res)

# if you didn't choose any option
else:
	# print error message
	print("\nERROR:\nEnter the correct arithmetic (1/2/3/4)!")
