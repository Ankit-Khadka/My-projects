# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# option = input("type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shif number.\n"))
#what should i do to encode this shiyt
# def ceaser(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     shift_amount == shift
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#         shifted_letter = alphabet.index(letter) + shift_amount
#         shifted_letter %= len(alphabet)
#         output_text += alphabet[shifted_letter]
#     print(f"Your {option} result is: {output_text}")

# ceaser(text,shift,option)
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
# Get user inputs


# Function to encode/decode text
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # Adjust shift amount if decoding
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    # Loop through each letter in the input text
    for letter in original_text:
        if letter in alphabet:
            # Find the position of the letter and apply shift
            shifted_letter = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_letter]
        else:
            # If character is not in alphabet, add it as is (e.g., spaces or punctuation)
            output_text += letter

    # Display the result
    print(f"Your {encode_or_decode}d result is: {output_text}")

second_choice = True 

while second_choice:




    option = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number.\n"))



# Call the function
    caesar(text, shift, option)
 
    if_want_to_play_again = input("Type 'yes' if you want to try again. Otherwise type 'no'.\n").lower()
    if if_want_to_play_again == "no":
        second_choice = False
        print("Goodbye!")