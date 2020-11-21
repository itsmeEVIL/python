# program to calculate your age base on the year you were born
# made by itsmeevil

import datetime

current_year = datetime.datetime.now().year

print("***Age Calculator***\n")

birthday = int(input("Enter the year you were born: "))
age = current_year - birthday

print("\nYour age is", age)
