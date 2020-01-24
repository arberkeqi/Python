age = 24
print("My age is %d years" % age)  # %d replaced by an int value that's provided after the str following %
major = "years"
minor = "months"

print("My age is %d %s and %d %s" % (age, major, 6, minor))     # to provide a string use %s
print("Pi is approximately %f" % (22 / 7))  # to inject a float into a string we'd use %f than provide a
# str and to get str us %s
print("Pi is approximately %60.50f" % (22 / 7))     # https://docs.python.org/2.4/lib/typesseq-strings.html
