a = 12            # the value 12 is assigned to the variable a
b = 3             # not an expression in the left of an assignment

print(a + b)      # 15
print(a - b)      # 9
print(a * b)      # 36
print(a / b)      # 4.0
print(a // b)     # 4 integer division, rounded down towards minus infinity
print(a % b)      # 0 modulo: the remainder after integer division

print()

for i in range(1, a // b):      # we have as an expression 1 and a // b
    print(i)
print()

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4 * 12))
print((((a + b) / 3)-4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)
