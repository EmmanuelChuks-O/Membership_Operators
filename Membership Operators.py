# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE" #string
#  in
letter = input("Guess a letter in the secret word: ").upper()
if letter in word:
    print(f"The {letter} is in the secret word")

else:
    print(f"The {letter} is not in the secret word")

# not in
letter = input("Guess a letter in the secret word: ").upper()
if letter not in word:
    print(f"The {letter} is not in the secret word")

else:
    print(f"The {letter} is in the secret word")

set
students = {"Emmanuel", "Oiza", "Chuks", "James", "Okoh"}

student = input("Enter a student name: ").capitalize()
if student in students:
    print(f"The {student} is in the class")

else:
    print(f"The {student} is not in the class")

# dictionary

grades = {"Emmanuel": "A",
          "Oiza": "B",
          "Chuks": "C",
          "James": "D",
          "Okoh": "E",}
student = input("Whose grade are you trying to find?: ").capitalize()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student}'s grade isn't available and the student is not registered.")

value = input("Type the grade and I'll locate the students in the system: ").capitalize()

if value in grades.values():
    print(f"The grade {value} is for {grades.values()}")