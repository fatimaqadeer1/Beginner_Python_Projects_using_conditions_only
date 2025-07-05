"""Description: Ask the user for their age. If age >= 18  
Eligible to vote, else not.
Concepts Used: if-else, int()"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
