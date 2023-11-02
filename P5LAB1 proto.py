# CTI 110
# P5LAB1 - CYOA
# Abdiel Ortiz
# 10/26/23
# Feel free to fork this REPL and make changes.

# first function: main_menu().

def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit] \n")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        # Call choice 2 here (You can add the corresponding function)
        choice_back_door()
    elif choice == '3':
        # Call choice 3 here (You can add the corresponding function)
        choice_go_home()
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()
       
# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home \n")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("Try to open the back door.")
    print("It creaks open...")
    print("Do you:")
    print("1. You enter the house.")
    print("2. Give up and go home \n")
    choice = input("Choose: ")
    if choice == '1':
      choice_enter_house()
    elif choice == '2':
      choice_go_home()
    else:
      print("You have to choose...")
      choice_back_door()

def choice_enter_house():
    print("You look behind you, the door is no longer there.")
    print("You are in a space of empty office rooms.")
    print("It's humid and dingy")
    print("It appears to be a maze")
    print("Do you:")
    print("1. Panic \n")
    choice = input("Choose: ")
    if choice == '1':
      choice_hope_eradicated()
    
    else:
      print("You have to choose...")
      choice_enter_house()

def choice_hope_eradicated():
     print("There is no escape in the endless maze, all you can do is hope. There is no hope...")

def choice_go_home():
    print("You live to tell another day...")

# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")

#start the program
main()


