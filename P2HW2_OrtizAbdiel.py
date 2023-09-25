#CTI- 110
#P2HW2- List
#Abdiel Ortiz
#9/24/23

grades = []

# range module 1-6
for module in range(1, 7):
    grade = float(input("Enter the grade for Module " + str(module) + ": "))
    grades.append(grade)
#append adds grade afterward
lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average_grade = sum(grades) / len(grades)
#str makes a string "f" instead of min/max data
lowest_grade_str = str(lowest_grade)
highest_grade_str = str(highest_grade)
total_grades_str = str(total_grades)
average_grade_str = str(average_grade)
#\n ends line
print("\nResults:")
print("Lowest Grade: " + lowest_grade_str[:4])
print("Highest Grade: " + highest_grade_str[:4])
print("Sum of Grades: " + total_grades_str[:4])
print("Average Grade: " + average_grade_str[:4])