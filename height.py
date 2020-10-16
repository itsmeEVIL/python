# program to calculate the average height of 5 members
# made by itsmeevil

# input
# height of first member
first = float(input('Height of the first member (Meter): '))
# height of second member
second = float(input('Height of the second member (Meter): '))
# height of third member
third = float(input('Height of the third member (Meter): '))
# height of fourth member
fourth = float(input('Height of the fourth member (Meter): '))
# height of fifth member
fifth = float(input('Height of the fifth member (Meter): '))

# proses
# total height of all member
total = first + second + third + fourth + fifth
# average height of all member
average = total / 5

# output
print('\nHeight Measurement Entered:')
# height of first member
print('First member: ', first, 'm')
# height of second member
print('Second member ', second, 'm')
# height of third member
print('Third member: ', third, 'm')
# height of fourth member
print('Fourth member: ', fourth, 'm')
# height of fifth member
print('Fifth member: ', fifth, 'm')
# average of all member
print('\nAverage Height: ', round(average, 2), 'm')
