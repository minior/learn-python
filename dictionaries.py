#in key-value pairs, not ordered ie. {a:b, x:y} == {x:y, a:b}
spam = {"me":"smart", "you":"stupid"}
bacon = {"you":"stupid", "me":"smart"}
print(spam == bacon) # true

for people in spam.keys():
    print(people)
for iq in spam.values():
    print(iq)
for pairs in spam.items(): #returns tuples (immutable)
    print(pairs) 

print(spam.get("them", 'x')) #get looks for key, if not returns x -> error catching
#note, these are ALL methods (works on spam)

spam.setdefault('him', 'average')
print(spam)
spam.setdefault('him', 'genius')
print(spam) #does not do anything because 'him' is already set

# we can also have a LIST of DICTIONARIES
cheese1 = {"type":"mozarella", "food":"cheese sticks", "rating":5}
all_cheese = [] #initiate list
all_cheese.append({"type":"cheddar", "food":"pizza", "rating":4})
all_cheese.append(cheese1)
print(all_cheese)

print(type(cheese1["type"])) #identify the type of data (only can be used on keys, NOT values)
print(type(cheese1))
print(type(all_cheese))
