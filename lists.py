supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for supply in range(len(supplies)):
    print('index '+ str(supply) + ' is ' + supplies[supply]) # supply is the index no.

#swapping variables!
a = "AAA"
b = "BBB"
print (a, b)
a, b = b, a
print (a, b)

#augmented assignment operators
spam = 1
spam = spam + 1
print (spam)
spam += 1
print (spam) #identical and preferred, vs $spam++; in php

#sort behaves weirdly -> ASCII order
spam = ['alpha', 'beta', 'Alpha', 'Beta', 'Zeal', 'zeal']
spam.sort()
print(spam)

spam.sort(key=str.lower) #keyword argument that does alphabetical order
print(spam)

#lists are mutable, created 'outside' the var -> the var only references this list
spam = [0, 1, 2, 3, 4, 5]
bacon = spam
print(bacon)
bacon[1] = "yolo"
print(bacon)
print(spam) # spam also changes! both spam and bacon ref. the SAME list

#avoidable with deepcopy() function
import copy
spam = [0, 1, 2, 3, 4, 5]
cheese = copy.deepcopy(spam) #this is a new list with the same values
cheese[1] = "swag"
print(cheese)
print(spam) #will not change