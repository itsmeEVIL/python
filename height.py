# program to calculate the average height of 5 members
# made by itsmeevil

first = float(input("Height of the first member (Meter): "))
second = float(input("Height of the second member (Meter): "))
third = float(input("Height of the third member (Meter): "))
fourth = float(input("Height of the fourth member (Meter): "))
fifth = float(input("Height of the fifth member (Meter): "))

average = (first + second + third + fourth + fifth) / 5

print("\nHeight Measurement Entered:")
print(f"First member: {first}m")
print(f"Second member {second}m")
print(f"Third member: {third}m")
print(f"Fourth member: {fourth}m")
print(f"Fifth member: {fifth}m")
print(f"\nAverage Height: {round(average, 2)}m")
