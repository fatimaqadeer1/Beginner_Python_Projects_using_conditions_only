""" Description: Ask user to enter a PIN. 
Check if it matches a stored PIN. If yes, allow access. If not, deny.
Concepts Used: input(), if-else"""

stored_pin = "1234"
entered_pin = input("Enter your PIN: ")

if entered_pin == stored_pin:
    print("Access granted.")
else:
    print("Incorrect PIN. Access denied.")
