"""Description: Ask the user to enter a color (red, yellow, green).
Print the action: 'Stop', 'Get Ready', 'Go'.
Concepts Used: input(), if-elif-else"""

color = input("Enter traffic light color (red, yellow, green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
