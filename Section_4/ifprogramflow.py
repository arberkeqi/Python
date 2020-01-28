# age = int(input("How old are you? "))
#
# # if (age >= 16) and (age <= 65):     # use parentheses to make the expression clearer
# #     if 15 < age < 66:
# #         print("Have a good day at works")
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
# # in Python true is one and false is zero, any non-zero or non-empty evaluate to true
# x = "false"
# if x:
#     print("x is true")
# x = input("Please enter some text ")
# if x:
#     print("You entered '{}".format(x))
# else:
#     print("You did not enter anything")
# print(not False)            # True
# print(not True)             #False
# age = int(input("How old are you? "))
# if not (age<18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back after {} years".format(18- age))
# print()
parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))
print()

name = input("What is your name? ")
age = int(input("How old are you? "))       # or int(input("How old are you {0}? ".format(name)))
if 18 <= age <= 30:
    print("Welcome to the holiday")
else:
    print("You are not in the age range, so better luck next time. ")

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capital = ''
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capital = capital + char
print("The CAPITAL LETTERS are {}. ".format(capital))

for i in range(0, 100, 7):
    print("{}".format(i))
