#python pizza
print("Welcome to the Ankit's pizza hub! ")
size = input("What size pizza do you want. S, M OR L ")
pepperoni = input("Do you want pepperoni in the pizza. Y or N ")
extra_cheese = input("Do you want cheese on your pizza. Y or N ")
#size
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You have enter the wrong data! ")

#pepperoni

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

#extra cheese

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}. ")
