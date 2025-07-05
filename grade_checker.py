""""Description: Ask user for a test score (0-100) and print the 
grade: A (90+), B (80-89), C (70-79), etc.
Concepts Used: if-elif-else"""

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
