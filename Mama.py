number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))

operator = input("Enter the matematical sign:")

correct_answer = 0
correct_input_counter = 0
wrong_input_counter = 0

print("Question:",number_one, operator, number_two)
match operator:
    case "+" : correct_answer = number_one + number_two
    case "-" : correct_answer = number_one - number_two
    case "x" : correct_answer = number_one * number_two

answer = float(input("Answer:"))
if correct_answer == answer:
    print("correct")
    correct_input_counter+=1

else:
    print("wrong")
    wrong_input_counter+=1

print(f"Number of wrong Answer is: {wrong_input_counter}")
print(f"Number of right Answer is: {correct_input_counter}")
