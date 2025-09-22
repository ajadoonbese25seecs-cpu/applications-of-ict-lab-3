marks = int(input("Enter your marks(0-100): "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks < 90:
    print("Grade B")
elif marks >= 50 and marks < 75:
    print("Grade C")
elif marks < 50 and marks >= 0:
    print("Grade F")
else:
    print("Invalid input")