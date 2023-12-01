# Project: simple tip calculator

print("Welcome to the tip calculator")

bill_amount = input("What was the total bill? £")

tip_percentage = input("What percentage tip would you like to give? 10%, 12%, or 15%? ")

number_of_people = input("How many people to split the bill? ")

tip_amount = int(tip_percentage) / 100 * float(bill_amount)

final_amount = tip_amount + float(bill_amount)

split_bill = final_amount / int(number_of_people)

rounded_number = round(split_bill, 2)

print(f"Each person should pay: £{rounded_number}")