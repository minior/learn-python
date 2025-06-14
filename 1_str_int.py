#strings are case-sensitive, so:
password = "abc"
answer = "ABC"
print(password == answer) #is false
print(password == answer.lower()) #now true

#string formatting
name = "John"
age = "20"
company = "vscode"
industry = "programming IDE software"
avail = "23 June"
print("Hi, my name is %s, I'm %s, and I am excited to apply for %s as I am excited about the %s industry. I will be available to start from %s." % (name, age, company, industry, avail))

# ask for name, print age, manipulate var type to avoid errors
import datetime as dt
this_year = dt.date.today().year

my_age = 25
print ("Hello There!\nWhat is your name?")
my_name = input()
print("Nice to meet you," + my_name)
print("The length of your name is: " + str(len(my_name)) + " letters.")
print("What is your age?")
try:                # catches error if user inputs text
    my_age = int(input())
    print("That means you were born in " + str((this_year - my_age)))
except:
    False

#join & split strings
animals = "; ".join(["cats", "dogs", "mouse"])
print(animals) #cats; dogs; mouse
print(animals.split("; ")) #['cats', 'dogs', 'mouse']

#ljust, rjust, centre -> wait its CENTER LOL
print(my_name.center(20,"~")) # ~~~~~~~~jack~~~~~~~~

#replace
spam="you are so smart"
print(spam.replace("so", "not"))
