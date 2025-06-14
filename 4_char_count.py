#simple code to count no. of each letter in a string
import pprint
string = """I have the high ground Anakin. 
You underestimate my power. 
You were supposed to destroy them not join them""" #use triple quotes for multiline strings (lines show up)
counter = {}
for letter in string.upper():
    counter.setdefault(letter, 0) #start from 0 on first appearance of letter
    counter[letter] = counter[letter] + 1 #no error because counter[letter] exists now
pprint.pprint(counter) #pprint sorts