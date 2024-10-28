#this is ganna be a fun code cuzz its hanging man game
hangman = ['''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |

=========''']
random_name = ["peach", "apple", "camel","banana", "cherry", "date", "grape", "mango", "orange", "papaya", "watermelon"]

# Randomly choose a word form the wordlist and assaign it a variable called chosen_word and print it
print("""                                               
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/           """)
import random
chosen_word = random.choice(random_name)
# print(chosen_word)


#ask the user to guess the letter and assign their guess to variable called guess. make guess lowercase.
place_holder = ""
choosen_word_in_length = len(chosen_word)
for position in range(0, choosen_word_in_length):
    place_holder += "_ "




#now i need to see if the guess is in the chosen_word genereted by the code
lives = 6
gameover = False
right_letters = []
while not gameover:
    guess = input("Please choose  words " + place_holder ).lower()

    if guess in right_letters:
        print(f"You have already guessed {guess} which is in the word! ")

    display = ""
    #how to keep track of lives in this game huhhhh howwwwwwwwww
    for letter in chosen_word:    
        if letter == guess:
            display += letter
            right_letters.append(letter,)
        elif letter in right_letters:
            display += letter
        else:
            display += "_"
        
    print(display)

    #todo list 2 keep track of lives
    if guess not in chosen_word:
        print(f"You have guessed {guess} which is not in the word! You have {lives} lives left.  ")
        lives -= 1
        if lives == 0:
            gameover = True
            print(f"You lose the word was {chosen_word}. Better luck next time!  ")





    if "_" not in display:
        gameover = True
        print("You Win!")

    print(hangman[lives])

    