my_list = list(range(10))
print(my_list)

even = list(range(0, 100, 2))
odd = list(range(1, 100, 2))
print(even)
print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"

print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)

print(small_decimals.index(3))

odd = range(1, 10000, 2)
print(odd)

print(odd[985])
print()
# sevens = range(7, 1000000, 7)
# x = int(input("PLease enter a positive number less than one million: "))
# if x in sevens:
#     print(f"{x}is divisible by seven")
# else:
#     print(f"{x} doesn't work")
#
# # slice ranges
# print(small_decimals)
#
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)
