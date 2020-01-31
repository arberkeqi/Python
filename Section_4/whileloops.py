# we need to keep looping as long as some condition is true and stop when it becomes false - using while loop.
# for i in range(10):           # in for loop no need to give a value cause it get itself
#     print(f"i is now  {i}")   # for loop for each item in a predetermined sequence
# i = 0
# while i < 10:           # in while loop need to give a value cause we get an error cause not defined
#     print(f"is is now {i}")   # while loop you don't need to know how many times the legal execute
#     i += 1
# available_exits = ["east", "north east", "south"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")  # an application is reading data in a file
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("Aren't you glad you got out of there!")      # while loop repeating til no data left

#                                           mine solution
# import random
# highest = 10
# answer = random.randint(1, highest)
#
# print(f"Please guess a number between 1 and {highest}: ")
# guess = int(input())
# while guess != answer:
#     if guess <= answer:
#         print("Please guess higher")
#     else:
#         print("Guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#         break
#     # else:
#     #     print("Sorry, you have not guessed it correctly")
# else:
#     print("You guessed it first time")

#                                           tim solution
import random
highest = 1000
answer = random.randint(1, highest)

print(f"Please guess a number between 1 and {highest}: ")
guess = 0
while guess != answer:
    guess = (int(input()))
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Guess lower")
    else:
        print("Well done, you guessed it")
