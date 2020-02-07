cast = ['Cleese', 'Idle', 'Gilliam', 'Jones', 'Palin', 'Chapman']
print(cast.sort())          # will print none. The sort function sorts the list in place, and returns None.

alpha1 = ["A", "B", "C", "D"]
alpha2 = ["A"]
alpha2.append("B")
alpha2.append("C")
alpha2.append("D")
print(alpha1 == alpha2)         # print - True. Both lists have the same items, in the same order.

trees = ["Larch", "Larch"]
identified_trees = trees
trees.append("Horse Chestnut")
print(identified_trees)     # There's only 1 list, and we appended "Horse Chestnut" to it. Whichever reference we use
# (trees or identified_trees), we get all 3 items appearing in the list.

flowers = [["rose", "red"], ["snapdragon", "white"], ["daisy", "white"], ["lily", "yellow"]]
second_flowers = flowers
second_flowers[1] = ["lilac", 'purple']
second_flowers[1][1] = 'pink'
print(flowers)

numbers = range(13)

new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')      # The new range starts at 1 and extends up to (but not including) 13, in steps of 2.
print()

even = range(0, 20, 2)
for number in even[::-1]:
    print(number, end=', ')     # The slice [::-1] reverses the range, which was counting from 0 up to (but not
    # including) 20, in steps of 2.

print()
print()

products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )
for product in products:
    name, product_type, company = product
    print(company)
print()
for i in products:
    print(i[2])

imelda = 'More Mayhem', 'Imelda May', 2011, ([
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')])
imelda[3].append((5, "All For You"))        # right way, not like - imelda[3].append(5, "All For You")
print(imelda[3])
