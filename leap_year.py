# program to know if this year is a leap year
# made by itsmeevil

# import time module for time delay
import time

print("***Leap Year Checker***")

year = int(input("\nEnter year: "))
print("Checking...")

time.sleep(2) # using the function sleep from time module to sleep for 2 seconds

if (year % 4) == 0:
	print("\nThe year entered is a leap year.")
	if (year % 100) == 0:
		print("\nThe year entered is not a leap year.")
	else:
		if (year % 400) == 0:
			print("\nThe year entered is a leap year.")
else:
	print("\nThe year entered is not a leap year.")
