# Learn Python Programming Masterclass

## Section 3

### helloworld.py
A function can take more than an argument.
######literal - a value of some type: 1) number - 423; 2) word - "Hello World"
######function - a named block of code that we can call by using its name, ex. print()
######argument - a value passed to a function, in order to give it values 

###string.py
If you have to use single quote like (') you need to enclose the string with double quote(")
and the other way around.
######input function - displays the text provided to it, then waits for text to be entered 

###escapechar.py (Escape character)
######backslash(\\) - is used to escape the character that follows it, to give that character special meaning. 
When we have **\n** it causes to start a new line, and **\t** tab the word (used for lists). We can
have a backslash in program if we add another backslash before or add an "**r**" before the quotes.

###Numeric data types
######int - integer the whole numbers, no fraction parts, stored in comp memory, no max size
######float - real numbers, have fractional parts, have 52 digits of precision 

###operators.py
Operators are: +; -, *, /, //,%(mbetja)
#####In Python an expression is anything that can be calculated to return a value

###string2.py
We can pick out single characters or some phrases that we want by using [:]. The counting starts from
0 from left to right and from -1 from right to left. When we make an index with negative numbers we 
need to start from left and go to right. But if we add to the index a negative like[::-1] we have 
to start writing the numbers from right to left. If we write [::no], we write this number to pass 
the values. When we write [::2] we pass the values by two etc.
#####Slicing
Produce a slice by providing three numbers separated colons. Numbers: 1) start; 2) stop; 3) step. 
The start value is the first value, the stop value is the last value.

###sliceback.py
The counting starts from -1 until the end of the variable counting from right to left.

###sequence_operators.py
5 types: 1) string; 2) list; 3) tuple; 4) range; 5) bytes and bytearrey. Sequence is defined as an 
order set of items. A list is also a sequence type. A sequence is ordered so we can use indexes to 
access individual item in the sequence. Everything that we can do with the string type sequence, we 
can do with every other sequence, with the exeption of range. Range cannot be concatenated or 
multiplied. print("Hello " * 5); print("Hello " * (5 + 4)); print("Hello " * 5 + "4");
print("he" in string1).

## Section 4

###tabs.py

###ifprogramflow.py

###forloops.py

## Section 5

###list.py
######We form a list by putting square brackets [ ]
List is a sequence of things and those things can be strings, numbers, classes or pretty much anything 
else. If a list can be a sequence of strings and a string is itself a sequence type, than it makes 
sense that a list can be a sequence of lists, which it can. Codes: .sort = doesn't return the sorted 
list, you put the sort this way cause we don't want to create new object; print(sorted(number)) -
this func returns the actual new object and sort the numbers. If you want to create a new object rather 
than sorting the one we have a built in func sorted(number)

###more_lists.py
By putting the command list() and enter an argument inside we form a list. Is we use to confirm if it 
is true or not and it differs from == because when we put == we imply that the values are the same, 
and when we put "is" we imply that the function is the same.

###challenge_list.py
How to put out some items out of a list

###iterators.py
An iterator is an object that represents a stream of a data. It actually returns the stream or the 
actual data in a stream, one element at a time. Iterable objects seen: 1) strings and 2) lists.
We can iterate by using the code iter('put the name of the list')

###ranges.py
In Python range is a built in type. In the simplest form create a range by specifying an n value.
ex. print(range(100)). 

###ranges_2.py

###tuples.py
Similar with lists, but the difference is that tuples are immutable(pandryshueshme), they can't be
changed. Attempting to append(shtoj) an item to a tuple will give an error. The comma is used to
separate the elements of a tuple, but the parentheses are required when necessary to remove syntactic
ambiguity. Tuples support indexing and slicing and use these to correct some typo in the code. It is 
not the variable immutable, but it's the object(the right side) that the variable points to. 

###demo.py(tuples)
We can give different values to a variable or multiple variables at the same time. E.x. a, b = 12, 13.

###tuples_2.py
Tuples can contain elements that are themselves tuples.
