# program to calculate the average from a list of numbers
# made by itsmeevil

def average(numList):
    return round(sum(numList) / len(numList), 2)

print("***Average Calculator***\n")

numList = input("Enter a list of numbers: ")
numList = numList.split(" ")
numList = list(map(float, numList))
average = average(numList)

print(f"\nThe average for the list of numbers entered: {average}")
