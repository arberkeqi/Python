# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         # continue        # continue= bypasses or stop processing for that particular expression
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

# # Modify the code inside this loop to stop when i is exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break

# for i in range(1, 20):
#     if i % 3==0 or i % 5==0:
#         continue
#     print(i)
