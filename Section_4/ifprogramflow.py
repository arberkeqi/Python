age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):     # use parentheses to make the expression clearer
#     if 15 < age < 66:
#         print("Have a good day at works")
if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")
# in Python true is one and false is zero, any non-zero or non-empty evaluate to true
x = "false"
if x:
    print("x is true")
