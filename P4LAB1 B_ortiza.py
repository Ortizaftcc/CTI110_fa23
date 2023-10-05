# CTI 110
# P4LAB 1 - Part B
# Text "graphics"
#ortiza
#10/5/23

# Draw a rectangle with text
CHAR = "🥴"
#print(CHAR)

# part 1: draw a horizontal line
WIDTH = int(input("How wide is the rectangle?"))
HEIGHT = int(input("How tall is it?"))
print("printing", WIDTH, "columns")
for column in range(WIDTH):
    # dont go to a new line
    print(CHAR, end="")

# part 2: vertical line
for row in range(HEIGHT):
    print(CHAR) # we want a new line


# part 3: darw a rectangle
for row in range(HEIGHT):
    for column in range(WIDTH):
        print(CHAR, end="")
    print() # end the line

