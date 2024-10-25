# #heads and tails
choice = input("If you want to flip the coin say. 'flip' ").lower()
if choice == "flip":
    import random
    number = random.randint(1, 2)
    if number == 1:
        print("Heads")
    else:
        print("Tails")
else:
    print("Sorry you have entered wrong instruction! ")


