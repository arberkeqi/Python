print("Today is a good day to learn Python.")
print('Python is fun.')
print("Python's strings are easy to use.")
print('We can even include "quotes" in strings.')
print("hello" + " world")
greeting = input("Please enter your greeting ")
name = "Arber"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old ")
print(type(age))

print(f"Pi is approximately {22/ 7:12.51}")    # same thing just he didn't use substitution using ".format"
print("Pi is approximately {0:12.50f}".format(22/7))    # but used the "f"(format) before the quotes in the expression
pi = 22 / 7
print(f"Pi is approximately {pi:50.51f}")      # the 12 to position it straight and after the "." no. after "."
