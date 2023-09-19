
"""
#Program to run travel expenses
#9/15/23
#CTI-110 P1HW2 - nTravel expense
#Abdiel Ortiz
"""


budget = 0
gas = 0
hotel = 0
food = 0
#total = (second, "+", third, "+", fourth, "=", second + third + fourth)
#balance = (total, "-", first, "=", total - first)


print(":Enter budget:")
budget = int(input())

print("Enter your travel destination:")
destination = input()

print("How much will you spend on gas?:")
gas = int(input())

print("Approximately, how much for hotel?:")
hotel = int(input())

print("How much will you need for food:")
food = int(input())

#balance = (first, "-", second, "-", third, "-", fourth, "=", first - second - third - fourth)
balance = (budget - gas - hotel - food)
#print(second, "+", third, "+", fourth, "=", second + third + fourth)

print("Travel expenses")
print("Destination:", destination)
print("Starting budget:", budget)
print("Gas:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print("Remaining balance:", balance)
