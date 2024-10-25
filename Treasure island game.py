#Treasure island game
print("Welcome to Treasure Island. Your mission is to find the treasure. ")
way_choice = input("You are at a double way road. choose where do you want to go left or right. ")
if way_choice == "left": #left is right answer
    print("You are in the edge of a lake!. ")
    if lake_choice == "wait": #just wait for the sailer to win
        print("You are going towards the middle of lake!")
        a_big_door = input("There is a big door with 2 material outside Armor and Torch! What do you want to pick up. type armor or torch ")
        if a_big_door == "torch":
            print("Yay you are able to see in the hall way and avoid the traps! ")
            small_door = input("Your are at the end of the hall way. There is two door's in front of you choose red door or  blue door. type red or blue ")
            if small_door == "red":
                print("Wow you are in the treasure room ")
                treasure_chest = input("There is two treasure chest in front of you old chest and new chest. choose old or new")
                if treasure_chest == "new":
                    print("You have found the treasure full of gold congrats! You have won ")
                else:
                    print("There was a monster hiding in the old chest you lost. Game over")
            else:
                print("The blue door was full of venomous gases you have died. Game Over ")
        else:
            print("You have died cause your armor could not save you from the traps! Game Over ")
    else:
        print("You have been eaten by pinranhas. Game Over!")
else:
    print("You have fallan into a hole!. Game Over!!!! ")
