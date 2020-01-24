letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]     # a slice [::-1] is a Python idiom
print(backwards)
backwards_1 = letters[-1::-2]
print(backwards_1)
print()
whatever = letters[3:18:4]
print(whatever)
print(letters[-25:2])
# slice the string to produce qpo
print(letters[16:13:-1])
print(letters[-10:-13:-1])
# slice the string to produce edcba
print(letters[4::-1])
print(letters[-22::-1])
# slice the string to produce last 8 characters, in reverse order
print(letters[25:17:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
