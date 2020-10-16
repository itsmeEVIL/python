# program to find out the number of calories allowed based on gender and age
# made by itsmeevil

# output
print('***RECOMMEND THE NUMBER OF CALORIES ALLOWED BASED ON GENDER AND AGE***')

# input
# gender (yes = male, no = female)
gender = input('Enter Your Gender (MALE/FEMALE): ')

# proses
# if gender is male
if gender.lower() == 'male':
	# input
	# age
	age = int(input('What Is Your Age? '))

	# if age more or equal to 60
	if (age >= 60):
		# output
		print('The allowed caloric value is 2010')

	# if age more or equal to 30
	elif (age >= 30):
		# output
		print('The allowed caloric value is 2460')

	# if age more or equal to 19
	elif (age >= 19):
		# output
		print('The allowed caloric value is 2440')

	# if age more or equal to 16
	elif (age >= 16):
		# output
		print('The allowed caloric value is 2840')

	# if age more or equal to 13
	elif (age >= 13):
		# output
		print('The allowed caloric value is 2690')

	# if age is less than 13
	else:
        # output
		print('Sorry, age limit must be 13 years and above.')

# if gender is female
elif gender.lower() == 'female':
	# input
	# umur
	age = int(input('What Is Your Age? '))

	# if age more or equal to 60
	if (age >= 60):
		# output
		print('The allowed caloric value is 1780')

	# if age more or equal to 30
	elif (age >= 30):
		# output
		print('The allowed caloric value is 2180')

	# if age more or equal to 19
	elif (age >= 19):
		# output
		print('The allowed caloric value is 2000')

	# if age more or equal to 16
	elif (age >= 16):
		# output
		print('The allowed caloric value is 2050')

	# if age more or equal to 13
	elif (age >= 13):
		# output
		print('The allowed caloric value is 2180')

	# if age less than 13
	else:
	    # output
		print('Sorry, age limit must be 13 years and above.')

# if there's no input or wrong input
else:
    # output
	print('ERROR:\nPlease Enter Your Gender Correctly!')
