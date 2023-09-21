#CTI 110
# M3 LAB1 - leap year
# ortiza
# 9/21/23

# Calculate if a year is a leap year
# leap years are:
#divisible by 4
#unless its a century, then its divisible by 400

# todo: handle the century case
is_leap_year = False

print("What year to check")
year = int(input())

# if the yer is divisible by 4, it is a leap year
# we use % the modulo operator
if year % 4 == 0:
  is_leap_year =  True

# century excetion:
# if its divisible by 100
if year % 100 == 0:
  # then it isnt a leap year
  is_leap_year = False
  # unless its also divisible by 400
  if year % 400 == 0:
    # and then it is a leap year
    is_leap_year = True
    

  #output the answer
if is_leap_year:
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")

