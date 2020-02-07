# list_1 = []
# list_2 = list()
#
# print(f"List 1: {list_1}")
# print(f"List 2: {list_2}")
# if list_1 == list_2:
#     print("The Lists are equal")
#
# print(list("The lists are equal"))       # by putting the command list() and enter an argument inside we form a list

# even = [2, 4, 6, 8]
# another_even = list(even)
# print(another_even is even)     # is we use to confirm if it is true or not
#
# another_even.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for numbers_set in numbers:
    print(numbers_set)
    for value in numbers_set:
        print(value)