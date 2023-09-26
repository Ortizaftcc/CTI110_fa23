"""
CTI 110
P3T2- choices and menus
Ortiza
9/26/23
"""
# the most simple, program
def main():
  #my_function()
  # *10 = "-" 10 times
  print("-"*10, "Main Menu", "-"*10)
  print("1. Option one")
  print("2. Option two")
  print("3. Option three")

  #Let user choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You chose:", choice)

  # branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
   option_2()
  elif choice == 3:
    option_3()
  else:
    print("Sorry, thats not an option.")
  
  
  
def option_1():
  print("Your at an intersection")
  print("Where do you turn")
  turn = input()
  if turn == "left":
    print ("You fall off a cliff and explode")
  elif turn == "right":
    print("You drive into a void.")
  else:
    print("...")
  
  
  

def option_2():
  print("You are at a zoo")
  print("What animal do you look at?")
  animal = input()
  if animal == "capybara":
    print("they are cute")
  elif animal == "sloth":
    print("he be hanging")
  else: 
    print("you have horrible taste")
  

def option_3():
  print("What game do you play")
  game = input()
  if game == "Terraria":
    print("install the calamity mod for peak progression.")
  else:
    print("Well theres always terraria")
  
# start the program
main()

