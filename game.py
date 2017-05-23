"""A number-guessing game. """

from random import randint

print "Howdy what's your name?"

user_name = raw_input("type in your name ")
random_num = randint(1, 100)
count = 0

while True:
    user_guess = int(raw_input("guess a number between 1 and 100: "))
    #if user_guess not in range(1, 101):
        print "Nice try.  Please enter a number between 1 and 100!! \n "
    if user_guess != random_num:
        if user_guess > random_num:
            print "Your number is too high, try again! \n "
            count += 1
        else:
            print "Your number is too low, try again! \n "
            count += 1

    else:
        print "Congrats! %s! You found my number in %i tries! " % (user_name, count)
        # print "Congrats! {}! You found my number in {}".format(user_name, count)
        break


# Put your code here
