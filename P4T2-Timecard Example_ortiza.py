# CTI 110
# P4T2 - time cards
# ortiza
# 10/5/23

# get the users work info for the week
# find the pay

#total = sum(data)
#count = len(data)
#avg = total/count
"""
hours = [8, 8, 8, 7, 9]
print("You worked:")
total_hours = sum(hours)
print(total_hours, "hours")
print("Longest shift was", max(hours), "hours")
print("shortest shift was", min(hours), "hours")
# find the average
average = total_hours / len(hours)
print("For an average of", average, "Hours per shift.")
"""

# Take 2 : by hand
print("Timecard program")
# set up variables
DAYS_OF_WEEK = 5 # constant
todays_hours = 0
total_hours = 0
# ask for time worked each day
# and take a running total
# we will print 1-5 instead of 0-4 (print(day))
for day in range(DAYS_OF_WEEK):
    print("Hours worked for day", day+1)
    todays_hours = float(input())
    #total_hours = total_hours + todays_hours #or,
    total_hours += todays_hours # shortcut += operator
    
# print the total and average hours
print("Total hours this week:" , total_hours)

average_hours = total_hours / DAYS_OF_WEEK
print("Average shift time:" , average_hours, "hours")
