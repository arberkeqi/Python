for i in range(0, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
# we use the "{replacement no. : and a number after}" that so we can have "the width" (space in the sentence)

print()

for i in range(0, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
# the "<" will left align and the ">" will right align and the "^" align the in the middle

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print()
for i in range(0, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print()

for i in range(0, 12):
    print("The no. {0:2} multiplying with 5 is {1:2} and dividing with 2 is {2:2}".format(i, i * 5, i / 2))
print()
quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])