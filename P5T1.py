# CTI 110
# P5T1 - Function
# ortiz
# 10/24/23

def main():
  print("Hello world!")
  burger = 4.9900001
  print_money(burger)
  print_money(12)
  print_money(0.3)
# main() ends when we stop indenting with tab

# other functions go here
def print_money(amount):
  print("$", format(amount, ".2f"), sep="")


# Now, start the program
main()
