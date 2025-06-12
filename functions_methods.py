# def, = function in PHP
def plus_one(num) :
    return num + 1
new_num = plus_one(5)
print(new_num)

def plus_one(num) :
    print (num + 1)
plus_one(5) # both works. Getting a value to be used elsewhere versus printing as part of the fn

#methods work on left side of .
spam = "hello there"
print(spam.upper())
print(spam) #strings are IMMUTABLE, spam isnt actually changed
spam = spam.upper() #unless I resassign
print(spam) 

#we can chain as well 
print(spam.upper().isupper()) #true

#startswith() and endswith()checks
spam = "hello there"
print(spam.startswith("hell"))
print(spam[1].startswith("e"))