alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#According to course 
import random
ran_letters = int(input("How many letters would you like to have in your password?\n"))
ran_number = int(input("How many numbers would you like in your password?\n"))
ran_symbol = int(input("How many symbols would you like in your password?\n"))
# password = ""
# for letters in range(1, ran_letters + 1):
#     password += random.choice(alphabets)
# for numbrs in range(1, ran_number + 1):
#     password += random.choice(numbers)
# for symbol in range(1, ran_symbol + 1):
#     password += random.choice(symbols)  
# print(password)
#hard way
password_list = []
for letters in range(1, ran_letters + 1):
    password_list.append(random.choice(alphabets))
for numbrs in range(1, ran_number + 1):
    password_list.append(random.choice(numbers))
for symbol in range(1, ran_symbol + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}!")



   

    