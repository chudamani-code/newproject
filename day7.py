# Dictionaries
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
#
# # Functions with outputs
#
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#
#     return f"{formatted_f_name} {formatted_l_name}"
#
# print(format_name("RajU", "NeuPaNe"))


# debugging

# problem 1

# number = int(input("which number do you want to check? \n"))
#
# if number % 2 = 0:
#     print("this ia an even number.")
# else:
#     print("this is an odd number.")

# solution
# number = int(input("which number do you want to check? \n"))
#
# if number % 2 == 0:
#     print("this ia an even number.")
# else:
#     print("this is an odd number.")


# problem 2
# year = input("which year do you want to check?")
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not lear year")

# solution
# year = int(input("which year do you want to check?"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not lear year")


# problem 3
# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("fizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

# solution
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)