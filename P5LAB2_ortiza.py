# CTI- 110
# P5LAB2 - Functions
# Ortiza
# 11/2/23

# first print a table of squares

def main():
  print("P5T2 - Squares")
  print("number\t\tnumber squared")
  # range (1,11) gives numbers 1-10
  for num in range(1,11):
    num_squared = square(num)
    print_row(num, num_squared)

    

def square(number):
  """inpurt: a number
  output a number squared."""
  square = number * number
  return square

#print_row()is a void function
def print_row(num, num_squared) :
    print(num, "\t", num_squared)

# Start program
main()