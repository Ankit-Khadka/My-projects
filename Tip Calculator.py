print("Welcome to tip calcuator!")
total_bill = float(input("What is the total amount of bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15"))
amount_of_people_who_split_bill = int(input("How many people would you like to split the bill? "))
total_amount = total_bill + tip
bill_per_person = total_amount/amount_of_people_who_split_bill
rounded_bill = round(bill_per_person, 2)
print(f"So each person has to pay: ${rounded_bill} each!")


            
