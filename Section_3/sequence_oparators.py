string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he" in string1)
print("he" in string4)

print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)        # True
print("fri" in today)        # True
print("thru" in today)       # False
print("parrot" in "fjord")   # False
# the in operators evaluates to True if the first thing exists in the second, and False otherwise.

my_family = ["une", "mami", "babi", "vllai"]
print(my_family[0][2])
