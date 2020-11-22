# program to find out the number of calories allowed based on gender and age
# made by itsmeevil

print("***RECOMMEND THE NUMBER OF CALORIES ALLOWED BASED ON GENDER AND AGE***")

gender = input("\nEnter Your Gender (MALE/FEMALE): ")
age = input("Enter your age: ")

if gender.lower() == "male":
	if age >= "60":
		print("\nThe allowed caloric value is 2010")
	elif age >= "30":
		print("\nThe allowed caloric value is 2460")
	elif age >= "19":
		print("\nThe allowed caloric value is 2440")
	elif age >= "16":
		print("\nThe allowed caloric value is 2840")
	elif age >= "13":
		print("\nThe allowed caloric value is 2690")
	else:
		print("\nSorry, age limit must be 13 years and above.")
elif gender.lower() == "female":
	if age >= "60":
		print("\nThe allowed caloric value is 1780")
	elif age >= "30":
		print("\nThe allowed caloric value is 2180")
	elif age >= "19":
		print("\nThe allowed caloric value is 2000")
	elif age >= "16":
		print("\nThe allowed caloric value is 2050")
	elif age >= "13":
		print("\nThe allowed caloric value is 2180")
	else:
		print("\nSorry, age limit must be 13 years and above.")
else:
	print("\nERROR:\nPlease Enter Your Gender Correctly!")
