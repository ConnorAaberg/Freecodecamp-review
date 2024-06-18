# lesson 11 -- Iterations: Definite Loops
# for i in [2,1,5]:
#     print(i)

# lesson 12 -- Iterations: Loop Idioms
# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# lesson 13 -- Iterations: more patterns

# count = 0
# sum = 0
# print('before', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
# 	count = count + 1
# 	sum = sum + value
# 	print(count, sum, value) 
# print('after', count, sum, sum / count)

# print('before')
# for value in [9, 41, 12, 3, 74, 15]:
# 	if value > 20:
# 		print('large number', value)
# print('after')

# found = False
# print('before', found)
# for value in [9, 41, 12, 3, 74, 15]:
# 	if value == 3:
# 		found = True
# 	print(found, value)
# print('after', found)

# longest_so_far = -1
# print('before', longest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
# 	if the_num > longest_so_far:
# 		longest_so_far = the_num
# 	print(longest_so_far, the_num)

# print('after', longest_so_far)

# smallest = None
# print('before')
# for value in [3, 41, 12, 9, 74, 15]:
# 	if smallest is None:
# 		smallest = value
# 	elif value < smallest:
# 		smallest = value
# 	print(smallest, value)

# print('after', value)

# lesson 14 -- Strings in Python

# fruit = 'banana'
# for letter in fruit:
# 	print(letter)

#	OR

# index = 0
# fruit = 'banana'
# while index < len(fruit):
# 	letter = fruit[index]
# 	print(letter)
# 	index = index + 1

# filter all 'a' out of str

# word = 'banana'
# count = 0
# for letter in word:
# 	if letter == 'a':
# 		count = count + 1 
# 	print(count)

# lesson 15 -- Intermediate Strings

# When slicing strings remember "up to but not including".

# by removing the first or last number of the slice we can start from beggining or end respectively

# lesson 16 -- Reading Files

# to start opening a file we use the open() funtion
# we tell python which file path to open, python returns a file handler variable to manipulate the file

# handle = open(filename, mode) 

# this retuns a handle to manipulate the file

# the filename should be a string containing the path to the file

# mode is either 'r' if we want to read the file or 'w' if we want to write in the file

# a newline character is a special character we use to indicate where a new line should start

# print('Hello\nWold')

# it is important to note that we use a backslash(\) instead of a forwardslash(/)

# a error will be called if a file does not exist

# lesson 17 -- Files as a Sequence

# xfile = open('test.txt')
# for cheese in xfile:
# 	print(cheese)

# fhand = open('test.txt')
# count = 0
# for line in fhand:
# 	count = count + 1
# print('line count:', count)

# fhand = open('test.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp)

# fhand = open('test.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	print(line)

# lesson 18 -- Python Lists

# friends = [ 'joseph', 'glenn', 'sally' ]

# carryon = [ 'socks', 'shirt', 'perfume' ]

# for friend in friends:
# 	print('Happy New Year', friend)
# print('Done!')

# x = [ 'joseph', 'glenn', 'sally' ]
# for x in x:
# 	print['Happy New Year', x]
# print('Done!')

# lesson 20 -- Working with Lists

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# # [1, 2, 3, 4, 5, 6]
# print(a)
# # [1, 2, 3]

# t = [9, 41, 12, 3, 74, 15]
# print(t[1:3])
# # [41:12]
# print(t[:4])
# # [9, 41, 12, 3]
# print(t[3:])
# # [3, 74, 15]
# print(t[:])
# # [9, 41, 12, 3, 74, 15]

# x = list()
# print(type(x))
# # <type 'list'>
# print(dir(x))
# # ['append', 'count', 'extend', 'index', 'insert',
# # 'pop', 'remove', 'reverse', 'sort']

# stuff = list()
# stuff.append('book')
# stuff.append('99')
# print(stuff)
# # ['book', 99]
# stuff.append('cookie')
# print(stuff)
# # ['book', 99, 'cookie']

# some = [1, 9, 21, 10, 16]
# 9 in 'some' list
# # true
# 15 in 'some' list
# # false
# 20 not in 'some' list
# # true