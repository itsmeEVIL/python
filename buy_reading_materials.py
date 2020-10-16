# program to calculate the price of the book

# variables
# price of books
# price of story book
story_book = float(39)
# price of magazine
magazine = float(16)

# proses
# total cost of story book and magazine
total1 = (story_book * 2) + magazine
# payment made
payment = 200
# remainder
remainder1 = 66

# total cost of all book
total_book_cost = payment - remainder1
# cost of 1 motivational book
motivational_book = (total_book_cost - total1) / 2

# calculation review
# total cost of all book
total2 = total1 + (2 * motivational_book)
# remainder
remainder2 = 200 - total2

# output
# payment made
print('Payment Made: RM200')
# cost of 2 story book
print('\nStory book: RM', 2 * story_book)
# cost of a magazine
print('Magazine: RM', magazine)
# cost of a motivational book
print('Motivational book: RM', motivational_book)
# remainder after payment was made
print('\nYour remainder: RM', remainder2, '\nCalculation review:', remainder2 == remainder1)
