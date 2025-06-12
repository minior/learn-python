import re #regex package

# \d, \w, \s -> digit, words+digits, spaces. also \D, \W, \S to mean NOT any \d,\w,\s respectively

# can create our own character classes
alpha_regex = re.compile(r"[a-zA-Z]") # same as r"(a|b|c|d...A|B|C|D... )"
not_alpha_regex = re.compile(r"[^a-zA-Z]") # "[^...]" means NOT, negating entire [] set

# ^ and $ can also mean 'start with' or 'ends with'
number = "90123344"
begin_with_9_regex = re.compile(r"^9")
print(begin_with_9_regex.search(number))
ends_with_4_regex = re.compile(r"4$")
print(ends_with_4_regex.search(number))

#using both ^ and $ can mean string must match, NOT contain
message = "90123344"
all_numbers = re.compile(r"^\d+$")
print(all_numbers.search(message))

phone_num_regex = re.compile(r"\d\d\d\d\d\d\d\d") #raw string, to ignore escape backslashes
match_object = phone_num_regex.search(message) #.search creates a match object
mo = match_object
print(mo.group()) # mo has method .group that returns the actual found values IF MATCHED

#we can also assign groups to the regex using brackets
phone_num_regex = re.compile(r"(\d)\d\d\d\d\d\d\d") #maybe i want to filter the first number, only identify singaporean numbers
mo = phone_num_regex.search(message) 
print(mo.group(1)) 

print(phone_num_regex.findall(message)) #findall directly returns a LIST / list of tuples if >1 group

# | is a pipe character, meaning OR
message = "JohnCena is hot" 
john_regex = re.compile(r"John(Wick|Cena|Connor)") #*note the surnames also forms a group
mo = john_regex.search(message) #mo returns false if no match (account for, in case of errors)
print(mo.group()) #JohnCena

# "()?" to notate optionals (either 0 or 1 time), 
message = "John is hot"
john_regex = re.compile(r"John(Wick)?")
mo = john_regex.search(message)
print(mo.group()) #John

# "()*" means at least 0 times, "()+" means at least 1 time, {x} means exactly x times
ha_regex = re.compile(r"(ha){3}")
print(ha_regex.search("you are so funny hahaha"))

# {x,y} means min x, max y -> either can be empty to denote only a min or max
ha_regex = re.compile(r"(ha){1,2}")
print(ha_regex.search("you are so funny hahahahahahaha")) #print haha because max 2

#regex matches are greedy -> use {x,y}? to match non-greedy
ha_regex = re.compile(r"(ha){1,4}?")
print(ha_regex.search("you are so funny hahahahahahaha")) #now prints ha since min of 1

# re.I optional argument for case-insensitive search
ha_regex = re.compile(r"(ha){1,4}?", re.I)
print(ha_regex.search("you are so funny HAHAHA"))

# . is wildcard, meaning "any char except newline"
ell_regex = re.compile(r".ells")
print(ell_regex.findall("she sells sea shells by the sea shore")) #['sells', 'hells'] 
# "(.*)" is commonly used to mean "0 or more of any chars except newline"
#or "(.*?)" for it to be non-greedy