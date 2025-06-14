#! python3
#above is a shebang line, telling windows to run it in the correc python version
#generate a random no. betw 1 & 10, user has 6 guesses
#in the end, this seems more complicated than it has to be. could have used break only for correct guess, and final attempt logic in a new if block

#ask for name
print ("Hey there gremlin, what's your name?")
while True:
    user_name = input()
    if len(user_name.replace(" ","")) == 0:
        print("err... I don't think you typed anything")
        continue
    elif user_name.replace(" ","").isalpha():
        break
    else:
        print("Unless you are X Æ A-12, sorry I assume your name has only letters in it")


# generate no.
import random
ans = random.randint(1, 10)

#allow user input
print ("Ok look, " + user_name + ", I'm thinking of a number between 1 and 10!")

#compare, then if elif flow control
for attempt in range(6):
    guess = input()
    if len(guess.replace(" ","")) == 0:
        print ("type something man... anything...")
        continue
    try: 
        guess = int(guess)
        if guess == ans:
            print ("good job! You took " + str(attempt + 1) + " attempts! You have been promoted to the rank of Imp")
            break
        elif guess < 1 or guess > 10:
            print ("I SAID BETWEEN 1 AND 10.")
            continue
        elif attempt < 5:
            if guess > ans:
                print ("too high!")
            elif guess < ans:
                print ("too low!")
    except:
        print ("NUMBERNUMBERNUMBER I SAID NUMBER!")
        continue
else:
    print ("good try, but my number was " + str(ans) + ". I once again display my superior wit.")