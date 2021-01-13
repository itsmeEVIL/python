# program to calculate the average from a list of numbers
# made by itsmeevil

def average(num_list):
    # sum() to sum up all the numbers
    # len() to calc the length of a list
    return sum(num_list) / len(num_list)

print("***Average Calculator***\n")

num_list = input("Enter a list of numbers: ")
num_list = num_list.split(" ") # put the nums into a list
num_list = list(map(float, num_list)) # map() to change the content of the list from str to float
average = average(num_list)

print(f"\nThe average for the list of numbers entered: {average}")
