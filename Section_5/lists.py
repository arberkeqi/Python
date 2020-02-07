# ip_address = input("Please enter an ip_address: ")
# print(ip_address.count("."))        # .count = counts the characters
parrot_list = ["non pining", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")
for state in parrot_list:
    print("This parrot is " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = even + odd
# number.sort()
number_in_order = sorted(number)       # this func returns the actual new object and sort the numbers
print(number_in_order)
# print(sorted(number))
# .sort = doesn't return the sorted list, you put the sort this way cause we don't want to create
# new object
# if you want to create a new object rather than sorting the one we have a built in func

if number == number_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if number_in_order == sorted(number):
    print("The lists are equal")
else:
    print("The lists are not equal")
