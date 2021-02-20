# program to calculate percentage increase
# made by itsmeevil

def percentageIncrease(startNumber, finalNumber):
    percentageIncrease = round(((finalNumber - startNumber) / startNumber) * 100, 2)
    return f"{percentageIncrease}%"

print("***Percentage Increase Calculator***\n")

startNumber = float(input("Enter the starting value: "))
finalNumber = float(input("Enter the final value: "))

print(f"\nThe percentage increase: {percentageIncrease(startNumber, finalNumber)}")
