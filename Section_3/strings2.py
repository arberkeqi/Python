parrot = "Norwegian Blue"
print(parrot)           # we can print a single letter, they start counting from zero
print(parrot[3])        # the number inside [] index(shows) a letter in the word that we have
print(parrot[4])
print(parrot[9])        # we can use the number of the index which is space or put print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[0:6])  # Norweg
print(parrot[-14:-8])
print(parrot[3:5])
print(parrot[-11:-9])
print(parrot[0:9])          # both lines(14:15) show us the same same thing
print(parrot[-14:-5])
print(parrot[:9])
print(parrot[:-5])
print(parrot[10:14])        # brackets [] are used for indexing and slicing
print(parrot[-4:15])
print(parrot[10:])
print(parrot[-4:])
print(parrot[:6])
print(parrot[:-8])
print(parrot[6:])
print(parrot[-8:])
print(parrot[:6] + parrot[6:])
print(parrot[:-8] + parrot[-8:])
print(parrot[:])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2])    # Nre we take the letters from 0 to 6(not including 6) step the sequences in step of 2
print(parrot[0:6:3])    # Nw we take the letters from 0 to 6(not including 6) step the sequences in step of 3
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print()
print(number[0::4])
