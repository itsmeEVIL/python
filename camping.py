# program to calculate the total cost of camping in uniformed units  

# variables
# cost of items in fixed cost
# cost of personal equipment
personal = float(13.50)
# cost of clothing
clothing = float(105.90)
# tent rental costs
tent = float(12.00)

# process
# fixed cost
fixed_cost = personal + clothing + tent
# cooking costs
cooking_cost = float(input('\nEnter the cost for cooking: RM'))
# total cost
total_cost = fixed_cost + cooking_cost

# output
print('\n***Calculation of Uniformed Unit Camping Cost***')
# total fixed cost
print('\nTotal of Fixed Cost: RM', fixed_cost)
# total costs change
print('Total of Changed Cost: RM', cooking_cost)
# total of all costs
print('Total of All Costs: RM', round(total_cost, 2))
