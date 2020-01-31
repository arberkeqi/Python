number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ''
# augmented assignment it's a short way of assigning values to a variable
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]   # concatenation and assigned to cleanNumber
        # cleanedNumber += number[i] instead
# python describes them as a single statement of binary operation and an assignment statement
# the concatenation is the binary operation, takes 2 upper ends to work
newNumber = int(cleanedNumber)
print(f"The number is {newNumber}")
x = 23
x += 1
# x = x + 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x //= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)
# two binary operators that can be performed on strings : concatenation and repetition

greeting = "good "
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)
print()

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number

print(answer)
