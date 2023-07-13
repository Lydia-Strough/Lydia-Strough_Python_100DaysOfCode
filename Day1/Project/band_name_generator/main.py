#TITLE: Band Name Generator (100 Days of Code, Day 1 Project)
#AUTHOR: Lydia Strough
#APPLICATION VERSION & DATE: Application Version 1.0, 07/13/2023

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
print("Your band name could be " + band_name)