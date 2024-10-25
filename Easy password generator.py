alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#start 
import random
print("Welcome to password generator! ")
ran_letters = int(input("How many letters would you like to have in your password?\n"))
ran_number = int(input("How many numbers would you like in your password?\n"))
ran_symbol = int(input("How many symbols would you like in your password?\n"))

#easy one
random_letters = random.choices(alphabets, k= ran_letters)
random_numbers = random.choices(numbers, k= ran_number)
random_symbols = random.choices(symbols, k= ran_symbol)
#Sum up of these choices
easy_password = random_letters + random_numbers + random_symbols
joint_password = result = ''.join(easy_password)
print(f"Your password could be {joint_password}!")