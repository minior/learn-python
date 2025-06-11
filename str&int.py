# ask for name, print age
import datetime as dt
this_year = dt.date.today().year

my_age = 25
print ("Hello There! \n What is your name?")
my_name = input()
print("Nice to meet you," + my_name)
print("The length of your name is: " + str(len(my_name)) + " letters.")
print("What is your age?")
my_age = int(input())
print("That means you were born in " + str((this_year - my_age)))
