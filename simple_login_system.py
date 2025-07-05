"""Description: Store a username and password in the script.
Ask the user to input them and check if both match.
Concepts Used: if-else, strings"""

stored_username = "user123"
stored_password = "pass123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login successful.")
else:
    print("Invalid username or password.")
