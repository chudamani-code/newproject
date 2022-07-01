# Data types
# 1) string  eg.: "Hello", "123"
# 2) integer eg.: 123, 4567777
# 3) float   eg.: 3.14159, 5.7, 0.0008
# 4) Boolean: True, False

# write a program that adds the digits in a 2 digit number. e.g. if input is 35, then output should be 3+5=8.
# two_digit_number = input("Enter 2 digit number: \n")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# result = first_digit + second_digit
# print(result)


# # calculate a BMI of a person:
# height = input("Enter your height in metre: \n")
# weight = input("Enter your weight in kg: \n")
# BMI = float(weight) / float(height) ** 2
# print("your BMI is:", BMI)

# round the number in specified places
print(round(8/3, 3))

# create a program to calculate how many weeks you have left if you will live for 90 not years

# age = int(input("Enter your current age: \n"))
# print(f"you have {90 - age} years or {(90 - age) * 52} weeks or  {(90 - age) * 365} days left")


# Tip calculator
total_bill = float(input("Enter total bill amount: \n"))
tip_percentage = int(input("Enter tip percentage you want to give, 10, 12 or 15: \n"))
number_of_people = int(input("Enter number of people: \n"))
each_should_pay = (total_bill + (tip_percentage * total_bill / 100)) / number_of_people
print("each person should pay", round(each_should_pay, 2))


