# Randamization and python lists

import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
new_float = random_float * 5
print(new_float)

# Heads or Tails game

import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")



# Banker roulette game

import random
import string

# names_string = input("Give me everybody's names, seperated by a comma. \n")  #raju, alisha, chudamani, loxmi, torpe
# names = names_string.split(", ")
# num_items = len(names)
# random_choices = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choices]
# print(person_who_will_pay + " is going to pay for the bill today.")

# nested lists

alphabet = ["abc", "def", "ghi", "jkl", "mno"]
numbers = ["1", "2", "3", "4", "5"]
string = [alphabet, numbers]
print(string)


# rock, paper, scissor game

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissor = '''

   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''

game_images = [rock, paper, scissor]
user_choice = int(input("type 0 for Rock, 1 for paper or 2 for scissor \n"))
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, you lose!!!")
else:
    print("you chose: " + game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("computer chose:")
    print(game_images[computer_choice])


    if user_choice >=3 or user_choice <0:
        print("you typed an invalid number, you loose!!")
    elif user_choice == 0 and computer_choice == 2:
        print("you win!!")
    elif computer_choice == 0 and user_choice ==2:
        print("you loose")
    elif user_choice > computer_choice:
        print("you win")
    elif computer_choice > user_choice:
        print("computer wins!!!")
    elif computer_choice == user_choice:
        print("Draw!!")
    elif user_choice >=3 or user_choice <0:
        print("you typed an invalid number, you loose!!")
