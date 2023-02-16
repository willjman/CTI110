# Travel buget
# 2/16/2023
# CTI-110 P1HW2 - Travel Expense
# William Johnson

print('This program calculates and displays travel expenses')
user_buget=int(input("\n"'Enter buget:'))
user_destination=input("\n"'Enter your travel destination:')
user_gas=int(input("\n"'How much do you think you will spend on gas?'))
user_accomodation=int(input("\n"'Approximately, how much will you need for accomodation/hotel?'))
user_food=int(input("\n"'Last , how much do you need for food?'))

print("\n"'--------Travel Expenses--------')
print('Location:', user_destination)
print('Initial Buget:', user_buget)

print("\n"'Fuel:', user_gas)
print('Accomodatiom:', user_accomodation)
print('Food:', user_food)
user_total=(user_gas + user_accomodation + user_food)
user_balance=(user_buget - user_total)
print("\n"'Remaining Balance:', user_balance)
