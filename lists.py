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