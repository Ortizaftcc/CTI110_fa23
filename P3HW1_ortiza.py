"""
CTI 110
P3HW1- Letter Grades
ortiza
9/28/23
"""

grades = []

#mod_1 = input("Enter grade for Moduele 1:")
#mod_2 = input("Enter grade for Moduele 2:")
#mod_3 = input("Enter grade for Moduele 3:")
#mod_4 = input("Enter grade for Moduele 4:")
#mod_5 = input("Enter grade for Moduele 5:")
#mod_6 = input("Enter grade for Moduele 6:")
  
for module in range(1,7):
  grade = float(input("Enter the grade for Module " + str(module) + ": "))
  grades.append(grade)
  print("grades so far = " , grades)
average_grade = sum(grades) / len(grades)

average_grade_str = str(average_grade)

print("Average Grade: " + average_grade_str[:4])


letter_grade ="G"

if average_grade >= 90:
  letter_grade = "A"
elif average_grade >= 80:
  letter_grade = "B"
elif average_grade >= 70:
  letter_grade = "C"
elif average_grade >= 60:
  letter_grade = "D"
else:
  
  letter_grade = "F"
  print(letter_grade)

print("A grade of", average_grade, "is a", letter_grade)