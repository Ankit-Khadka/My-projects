#Trial
print("Welcome to rollercoaster ride! ")
height = int(input("Please enter your height. "))
bill = 0
if height >= 130:
    print("You are eligible to enter the ride. ")
    age = int(input("Please enter you age for the price of the ride! "))
    if age <= 14:
        bill = 4
        print("Child ticket is  $4. ")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7. ")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is $0. ")
    else:
        bill = 11
        print("Adult ticket is  $11.")
    photo = input("Do you want to click photos if Yes type y if no type n. ")
    if photo == "y":
        total_bill = bill + 3
        print(f"Your total price for the ticket is ${total_bill}.")
    else:
        print(f"Your total bill is {bill}.")
else:
    print("Sorry please come again next time once you grow.")