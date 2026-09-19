grade_one = int(input("Enter the first number:"))
grade_two = int(input("Enter the second number:"))
grade_three = int(input("Enter the third number:"))
grade_four = int(input("Enter the fourth number:"))

grade = [grade_one, grade_two, grade_three, grade_four]
print(sorted(grade))
import statistics
print(statistics.median(grade))

