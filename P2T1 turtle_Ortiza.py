import matplotlib.pyplot as plt
import turtle

# Collect data
data = [] # empty list
# New version - Loop and get each day at a time
#num_days = int(input("how many days? "))
num_days = turtle.numinput("input", "How many days? ")
num_days = int(num_days)
for day in range(num_days):
  #print("Day ", day, ":", end="")
  #today = int(input())
  label = "Day #" + str(day) # "day 1" and so on
  today = turtle.numinput("Next day", "How many pokeman?")
  data.append(today) # add it to the end of the list

# put the data in a list(done)
# print min and max
print()
print("best day:", max(data))
print("Worst day:", min(data))
# TODO total and average
total = 0
for num in data:
  total += num
  #total is now all numbers in data added up
average = total / num_days
print("total:", average)
print("average:", average)

# Graph the data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("pokeman data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()

