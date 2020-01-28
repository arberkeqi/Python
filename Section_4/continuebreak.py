# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         # continue        # continue= bypasses or stop processing for that particular exppression
#         break             # break - stops the operating under that point(til that point no more)
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")
if nasty_food_item:
    print("Can't I have anything without spam in it")
