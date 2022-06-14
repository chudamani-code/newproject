# control flow and logical operators

# write a program to find a given number is even or odd

# number = int(input("Enter a number: \n"))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")


# BMI calculator 2.0

# height = input("Enter your height in metre: \n")
# weight = input("Enter your weight in kg: \n")
# BMI = float(weight) / float(height) ** 2
# print("your BMI is:", round(BMI))
#
# if BMI < 18.5:
#     print("underweight!!!")
# elif BMI <25:
#     print("Normal Weight!!!")
# elif BMI <30:
#     print("Overweight!!!")
# elif BMI <35:
#     print("Obese!!")
# else:
#     print("Clinically obese... get medical help!!")


# how to find a leap year

# year = int(input("Enter any year you want to test: \n"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print ("Leap year!!")
#         else:
#             print("Not a leap year!!")
#     else:
#         print("Leap Year!!")
# else:
#     print("Not Leap Year!!!")


# Pizza order

# print("welcome to Raju's Pizza")
# size = input("what size you want? S, M or L: \n")
# add_pepperoni = input("Do you want to add pepperoni? Y or N: \n")
# extra_cheese = input("Do you want to add extra cheese? Y or N: \n")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"your final bill is ${bill}")

# Love calculator
#
# print("welcome to love calculator")
# name1 = input("enter name1: \n")
# name2 = input("enter name2: \n")
# combined_name = name1 + name2
# lower_case_name = combined_name.lower()
#
# t = lower_case_name.count("t")
# r = lower_case_name.count("r")
# u = lower_case_name.count("u")
# e = lower_case_name.count("e")
#
# true = t + r + u + e
#
# l = lower_case_name.count("l")
# o = lower_case_name.count("o")
# v = lower_case_name.count("v")
# e = lower_case_name.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
# if (love_score < 10) or (love_score > 90):
#     print(f"your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"your score is {love_score}, you are alright together.")
# else:
#     print(f"your score is {love_score}")


# treasure island    find ascii art on: ascii.co.uk/art

# print(''' _.--.
#                         _.-'_:-'||
#                     _.-'_.-::::'||
#                _.-:'_.-::::::'  ||
#              .'`-.-:::::::'     ||
#             /.'`;|:::::::'      ||_
#            ||   ||::::::'     _.;._'-._
#            ||   ||:::::'  _.-!oo @.!-._'-.
#            \'.  ||:::::.-!()oo @!()@.-'_.|
#             '.'-;|:.-'.&$@.& ()$%-'o.'\U||
#               `>'-.!@%()@'@_%-'_.-o _.|'||
#                ||-._'-.@.-'_.-' _.-o  |'||
#                ||=[ '-._.-\U/.-'    o |'||
#                || '-.]=|| |'|      o  |'||
#                ||      || |'|        _| ';
#                ||      || |'|    _.-'_.-'
#                |'-._   || |'|_.-'_.-'
#             jgs '-._'-.|| |' `_.-'
#                     '-.||_/.-'
#                     ''')
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("you\'ve arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which one will you pick?\n").lower()
        if choice3 == "red":
            print("it's a room full of fire. Game Over")
        elif  choice3 == "yellow":
            print("Ahoy!!! you've found the treasure")
        elif choice3 == "blue":
            print("it's a room full of beasts. Game Over")
        else:
            print("you chose a door that doesn't exist. game over.")
    else:
        print("you got attacked by sharks. game over.")
else:
    print("Game over: you fucked up and fell into a hole")
