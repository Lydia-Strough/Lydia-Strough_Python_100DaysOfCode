#TITLE: Tip Calculator (100 Days of Code, Day 2 Project)
#AUTHOR: Lydia Strough
#APPLICATION VERSION: 1.0
#DATE: 07/26/2023

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * (tip_percent / 100))
#Round total to 2 decimal places (E.g., 55.00)
bill_per_person = round(bill_with_tip / people, 2)
#If both decimal places are "0", formating is required so Python doesn't delete the second "0"
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")