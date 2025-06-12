import re

# sub(replacement, target)
names_regex = re.compile(r"Agent (\w+)")
message = "Agent Perry is the mole"
print(names_regex.findall(message))
print(names_regex.sub("REDACTED", message))

# to replace part of the match
names_regex = re.compile(r"Agent (\w)\w*")
message = "Agent Perry is the mole"
print(names_regex.findall(message))
print(names_regex.sub(r"Agent \1****", message))

# re.VERBOSE means ignore whitespace & newlines
number1 = "+65 9001 1234"
number2 ="6590011234"
phone_regex = re.compile(r'''\+{,1}\d\d # area code
\s*         #optional space
\d\d\d\d    #4 digits
\s*         #optional space
\d\d\d\d    #last 4 digits''', re.VERBOSE)
print(phone_regex.findall(number1))
print(phone_regex.findall(number2))

#can also do ",re.VERBOSE | re.I | re.DOTALL" to include multiple optional keyword arguments
#note | does not mean OR elsewhere, unlike in PHP