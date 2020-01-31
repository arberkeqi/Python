# for i in range(1, 20):
#     print("i is now {}".format(i))
# print()
# number = "9, 223, 372, 036, 854, 775, 807"
# for i in range(0, len(number)):         # len - length
#     print(number[i])
# print()
# number = "9, 223, 372, 036, 854, 775, 807"
# cleanedNumber = ''

# for i in range(0, len(number)):
#     if number[i] in '0123456789':     ; if i is in the range of these numbers and this way we not comma
#         cleanedNumber = cleanedNumber + number[i]
#         # print(number[i], end='')    by typing end='' we overwrite the end=\n(begin new line)
# convert from a string to an integer
# newNumber = int(cleanedNumber)
# print("The number is {}. ".format(newNumber))

number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ''
for char in number:  # char- will extract a character that each position in that number string
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pining", "no more", "a stiff", "bereft of life"]:  # list of string
    print("This parrot is " + state)
    # print("This parrot is {}".format(state))
for i in range(0, 100, 5):
    print(f"i is {i}")

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}. ".format(i, j, i * j), end="\t")
    print("==================")
    print("")
