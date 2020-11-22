# program to calculate the total cost of camping in uniformed units  
# made by itsmeevil

personal = float(13.50)
clothing = float(105.90)
tent = float(12.00)

fixed_cost = personal + clothing + tent
cooking_cost = float(input("\nEnter the cost for cooking: RM "))
total_cost = fixed_cost + cooking_cost

print("\n***Calculation of Uniformed Unit Camping Cost***")
print(f"\nTotal of Fixed Cost: RM {fixed_cost}")
print(f"Total of Changed Cost: RM {cooking_cost}")
print(f"Total of All Costs: RM {round(total_cost, 2)}")
