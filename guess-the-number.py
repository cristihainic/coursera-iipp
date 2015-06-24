import simplegui
import random

# global variables
num_guesses = 0
num_range = 101
secret_number = 0

# helper function to start and restart the game
def new_game():
    global num_guesses
    global num_range
    global secret_number
    if num_range == 101:
        num_guesses = 7
        secret_number = random.randrange (0, 101)
        print "\nNew game started. Range is from 0 to 100."
        print "Number of guesses left: %r." %num_guesses
    elif num_range == 1001:
        num_guesses = 10
        secret_number = random.randrange(0, 1001)
        print "\nNew game started. Range is from 0 to 1000."
        print "Number of guesses left: %r." %num_guesses
    else:
        print "ERROR! Check code!"   

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 101
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global num_range
    num_range = 1001
    new_game()
    
def input_guess(guess):
    global num_guesses
    global secret_number
    guess = int(guess)
    print "Your guess was %d." % guess
    if guess < secret_number:
        print "Higher!"
        num_guesses -= 1
        if num_guesses == 0:
            print "You kinda suck at this game."
            new_game()
        print "Number of guesses left: %r." %num_guesses
    elif guess > secret_number:
        print "Lower!"
        num_guesses -= 1
        if num_guesses == 0:
            print "You kinda suck at this game."
            new_game()
        print "Number of guesses left: %r." %num_guesses
    elif guess == secret_number:
        print "Correct!"
        new_game()
    else:
        print "ERROR! Check code!"
    
# create frame

f = simplegui.create_frame("Guess the Number!", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Guess from 100", range100, 200)
f.add_button("Guess from 1000", range1000, 200)
f.add_input("Your guess here:", input_guess, 200)

# call new_game 
new_game()
f.start()


# always remember to check your completed program against the grading rubric
