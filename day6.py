# function with parameters


# paint area calculator
# import math
#
#
# def paint_calc(wall_height, wall_width, cover):
#     area_of_wall = wall_height * wall_width
#     no_of_can_needed = math.ceil(area_of_wall / cover)
#     print(f"you'll need {no_of_can_needed} can of paint.")
#
# test_h = int(input("Height of the wall: "))
# test_w = int(input("Width of the wall: "))
# coverage = 5
#
# paint_calc(test_h, test_w, coverage)


# prime number checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is a prime number.")
#     else:
#         print("It is not a prime number")
#
# n = int(input("check this number: "))
# prime_checker(number=n)



# ceaser cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)

    result = input("type 'yes' if you want to go again. otherwise type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Goodbye!!!")
