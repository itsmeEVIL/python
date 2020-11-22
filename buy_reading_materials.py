# program to calculate the price of the book
# made by itsmeevil

story_book = float(39)
magazine = float(16)

total1 = (story_book * 2) + magazine
payment = 200
remainder1 = 66

total_book_cost = payment - remainder1
motivational_book = (total_book_cost - total1) / 2

total2 = total1 + (2 * motivational_book)
remainder2 = 200 - total2

print("Payment Made: RM200")
print(f"\nStory book: RM {2 * story_book}")
print(f"Magazine: RM {magazine}")
print(f"Motivational book: RM {motivational_book}")
print(f"\nYour remainder: RM {remainder2}\nCalculation review: {remainder2 == remainder1}")
