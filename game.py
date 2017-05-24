"""A number-guessing game. """

from random import randint


print "Howdy what's your name?"

user_name = raw_input("type in your name ")
random_num = randint(1, 100)
count = 0

while True:
    # user_guess = raw_input("guess a number between 1 and 100: ")
    try:
        user_guess = int(raw_input("guess a number between 1 and 100: "))
        #fix me complete : If a user enters a decimal, inform the user that you rounded their number. Round the number and keep playing
        # user_guess = float(raw_input("guess a number between 1 and 100: "))
        
      
    except ValueError:
        print("Heyyyy, put in a N U M B E R! \n ")
        continue
 #if user_guess not in range(1, 101):
       # print "Nice try.  Please enter a number between 1 and 100!! \n "
    if "." in user_guess:
        print "You entered a float, we rounded your number."
        #fixme
        # user_guess = int(round(float(user_guess)))
        # user_guess = round(user_guess)

        print user_guess

    if user_guess < 1 or user_guess > 100:
        print "Nice try! Try again! "

    elif user_guess != random_num:
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

# to complete  do " If a user enters a decimal, inform the user that you rounded their number. Round the number and keep playing "
#do:"
# Put your code here
# user_guess = raw_input("guess a numb") #  << outside  try
#user_guess_int = int(round(float(user_guess)))