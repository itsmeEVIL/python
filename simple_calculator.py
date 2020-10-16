print("***A Simple Calculator***\n\nCalculator to calculate 2 numbers\nOptions:\n1. Addition (+)\n2. Subtraction (-)\n2. Multiply (x)\n4. Divide (÷)\nNote - You can only choose 1 of the 4 options\n")

num1 = input("Enter the first number: ")
arithmetic = input("Enter the option (1/2/3/4): ")
num2 = input("Enter the second number: ")

def isFloat(value):
	try:
		float(value)
		return True
	
	except ValueError:
		return False

if num1 != "" and num2 != "":
	if isFloat(num1) == True and isFloat(num2) == True:
		num1 = float(num1)
		num2 = float(num2)
		if arithmetic == "1":
			res = num1 + num2
			print("\nCalculation:\n", num1, "+", num2, "=", res)
			print("\nResult:\nThe sum of", num1, "and", num2, "is", res)
		
		elif arithmetic == "2":
			res = num1 - num2
			print("\nCalculation:\n", num1, "-", num2, "=", res)
			print("\nResult:\nThe subtraction of", num1, "and", num2, "is", res)
		
		elif arithmetic == "3":
			res = num1 * num2
			print("\nCalculation:\n", num1, "x", num2, "=", res)
			print("\nResult:\nThe multiplication of", num1, "and", num2, "is", res)
			
		elif arithmetic == "4":
			res = num1 / num2
			print("\nCalculation:\n", num1, "÷", num2, "=", res)
			print("\nResult:\nThe division of", num1, "and", num2, "is", res)
			
		else:
			print("\nERROR:\nEnter the correct arithmetic (1/2/3/4)!")
			
	elif isFloat(num1) == False and isFloat(num2) == True:
		print("\nERROR:\nEnter the first number correctly (NUMBER)!")

	elif isFloat(num1) == True and isFloat(num2) == False:
		print("\nERROR:\nEnter the second number correctly (NUMBER)!")

	else:
		print("\nERROR:\nEnter the first and the second number correctly (NUMBER)!")

elif num1 == "" and num2 != "":
	print("\nERROR:\nEnter the first number!")

elif num1 != "" and num2 == "":
	print("\nERROR:\nEnter the second number!")

else:
	print("\nERROR:\nEnter the first and the second number!")
