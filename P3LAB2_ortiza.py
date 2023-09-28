"""
CTI 110
P3LAB2 - Letter Grades
ortiza
9/28/23

Convert a number into a letter grade
"""

print("Enter the number grade:", end="")
num_grade = int(input())

letter_grade = "G"

if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else:
  
  letter_grade = "F"
  print(letter_grade)
  


#print the letter grade
print("A grade of", num_grade, "is a", letter_grade)

