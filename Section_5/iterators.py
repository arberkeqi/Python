string = "1234567890"
# number = sorted(string)
# print(number)
# for char in string:
#     print(char)

# behind the scenes is there an iterator that's created from a string and the for loop uses that iterator to return
# each item of the string and when they are normal items iterator returns an error and the for loop actually terminates

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
# # do the same thing, 2nd ex show what happen in the 1st, the for is creating an iterator
# for char in iter(string):
#     print(char)

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

iterator = iter(numbers)
for i in range(0, len(numbers)):
    item = next(iterator)
    print(item)

print('='*80)

for item in iter(numbers):
    print(item)

print('='*80)
for item in numbers:
    print(item)
print('='*80)

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
