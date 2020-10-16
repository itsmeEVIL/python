# program to calculate 2 numbers
# made by itsmeevil

# print the available options
print("***A Simple Calculator***\n\nCalculator to calculate 2 numbers\nOptions:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (x)\n4. Division (÷)\nNote - You can only choose 1 out of the 4 options\n")

# input 1st num
num1 = input("Enter the first number: ")
# input option choosen
arithmetic = input("Enter the option (1/2/3/4): ")
# input 2nd num
num2 = input("Enter the second number: ")

# function to check whether a value is a float
def isFloat(value):
	try: # if the value is a float - return true
		float(value)
		return True
	
	except ValueError: # if the value is not a float - return false
		return False

# check if you entered anything
# if you did enter 1st and 2nd num
if num1 != "" and num2 != "":
	# check if what you entered is a num or not
	# if 1st and 2nd num is a num
	if isFloat(num1) == True and isFloat(num2) == True:
		# convert str to float
		num1 = float(num1)
		num2 = float(num2)
		
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
	
	# if 1st num isn't a num
	elif isFloat(num1) == False and isFloat(num2) == True:
		# print error message
		print("\nERROR:\nEnter the first number correctly (NUMBER)!")
		
	# if 2nd num isn't a num
	elif isFloat(num1) == True and isFloat(num2) == False:
		# print error message
		print("\nERROR:\nEnter the second number correctly (NUMBER)!")
	
	# if 1st and 2nd num isn't a num
	else:
		# print error message
		print("\nERROR:\nEnter the first and the second number correctly (NUMBER)!")
	
# if you didn't enter the 1st num
elif num1 == "" and num2 != "":
	# print error message
	print("\nERROR:\nEnter the first number!")

# if you didn't enter the 2nd num
elif num1 != "" and num2 == "":
	# print error message
	print("\nERROR:\nEnter the second number!")

# if you didn't enter anything
else:
	# print error message
	print("\nERROR:\nEnter the first and the second number!")
