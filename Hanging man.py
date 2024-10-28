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
import random
chosen_word = random.choice(random_name)
print(chosen_word)


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
        lives -= 1
        if lives == 0:
            gameover = True
            print("You lose")




    if "_" not in display:
        gameover = True
        print("You Win!")

    print(hangman[lives])

    