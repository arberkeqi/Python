# decimals = range(0, 100)
# print(decimals)
#
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 5, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
# print('='*60)
# for i in range(99, 0, -2):
#     print(i)
# print('='*60)
#
# print(range(0, 100)[::-2]== range(99, 0, -2))
# for i in range(100, 0, -2):
#     print(i)

# backstring = ".egaugnal lufrewop yrev a si nohtyP"
# print(backstring[::-1])
# string = "Python is a very powerful language."
# print(string[::-1])
#
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
print('=' * 80)

for i in iter(o):
    print(i)
print('=' * 80)

for i in p:
    print(i)

print('=' * 80)

for i in o:
    print(i)
print('=' * 80)

q = p[::-2]
print(q)

for i in q:
    print(i)
