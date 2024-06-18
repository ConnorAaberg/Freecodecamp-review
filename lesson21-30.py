# # lesson 21 -- Strings and Lists

# line = 'a lot                                     of spaces '
# etc = line.split()
# print(etc)
# # ['a', 'lot', 'spaces']

# line = 'first;second;third'
# thing = line.split()
# print(thing)
# # ['first;second;third']
# print(len(thing))

# thing = thing.split(':')
# print(thing)
# # ['first', 'second', 'third']
# print(len(thing))

# lesson 22 -- Python Dictionaries

# # every item stored in a dictionary has a 'key' which is used to access the stored item

# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# # {'money': 12, 'candy': 3, 'tissues': 75}
# print(purse['candy'])
# # 3
# purse['candy'] = purse['candy'] + 2
# print(purse['candy'])

# # lesson 23 -- Dictionaries: Common Applications

# # a common use for dictionaries is to make histograms with them, a histogram counts the frequency of certain items

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# # {'csev' : 1, 'cwen' : 1}
# ccc{'cwen'} = ccc['cwen'] + 1
# print(ccc)
# # {'csev' : 1, 'cwen' : 2}

# # lesson 24 -- Dictionaries and loops

# counts = dict()
# print('{ ↓ INSERT TEXT HERE ↓ }')
# line = input('')

# word = line.split()

# print('words:', words)

# print('counting...')
# for word in words:
# 	counts[word] = counts.get(word,0) + 1
# 	print('counts', counts)

# # NOTE: this will not work on sublime text because
# # you cannot interact with the terminal. 

# jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
# print(list(jjj.keys()))
# # ['jan' , 'chuck' , 'fred' ]
# print(jjj.values())
# # [100 , 1 , 42]
# print(jjj.items())
# # [ ('chuck' : 1) , ('fred' : 42) , ('jan' : 100) ]

# # lesson 24 -- The Tuple Collection

# # tuples are lists except they cannot be modified within the code

# # tuples can also be used in siuations like this --> (x, y) = (99, 98)
# # x = 99, y = 98

# # lesson 25 -- The Tuples Collection

# # a tuple is a list that cannot be changed in the code

# # lesson 26 -- comparing and sorting tuples

# d = {'a': 10, 'b': 1, 'c': 22}
# print(d.items)
# # ([('a', 10), ('c', 22), ('b', 1)])

# print(sorted(d.items()))
# # ([('a', 10), ('b', 1), ('c', 22)])

# d = {'a': 10, 'b': 1, 'c': 22}
# t = sorted(d.items())
# print(t)
# # [{'a': 10, 'b': 1, 'c': 22}]
# for k, v in sorted(d.items())
# print(k, v)

# # a 10
# # d 1
# # c 22

# c = {'a': 10, 'b': 1, 'c': 22}

# tmp = list()
# for k, v in c.items() :
# 	tmp.append( (v, k) )

# print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]
# tmp = sorted(tmp, reversed=true)
# # [(22, 'c'), (10, 'a'), (1, 'b')]

# lesson 27 -- Regular Expressions

# import re

# # ^         Matches the begginning of a line
# # $         Matches the end of a line
# # .         Matches any character
# # \s        Matches whitespace
# # \S        Matches any non-whitespace character
# # *         Repeats a character zero or more times
# # *?        Repeats a character zero or more times (non-greedy)
# # +         Repeats a character one or more times
# # +?        Repeats a character one or more times (non greedy)
# # [aeiou]   Matches a single character in the listed set
# # [^xyz]    matches a single character not in the listed set
# # [a-x0-9]  The set of characters can include a range
# # (         Indicates where string extraction is to start
# # )         Indicates where string extraction is to end

lessson 28 -- Regular Expression: Matching and Extracting Data
