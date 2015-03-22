import simplegui
import random

#initialize global variables
num_range = 100
num_of_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, num_of_guesses
    secret_number = random.randrange(num_range)
    print "NEW GAME"
    if num_range == 100:
        num_of_guesses = 7
        print "Range is 0 to 100, you're allowed %s guesses\n" % (num_of_guesses)
    else:
        num_of_guesses = 10
        print "Range is 0 to 1000, you're allowed %s guesses\n" % (num_of_guesses)

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global num_of_guesses
    int_guess = int(guess)
    print "You guessed %s" % (int_guess)

    if secret_number > int_guess:
        num_of_guesses -= 1
        print "Higher"
        print "%s guesses remaining\n" % (num_of_guesses)
    elif secret_number < int_guess:
        num_of_guesses -= 1
        print "Lower"
        print "%s guesses remaining\n" % (num_of_guesses)
    else:
        print "Correct!\n"
        new_game()
    
    if num_of_guesses == 0:
        print "Sorry, you did not guess the number"
        print "GAME OVER\n"
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 150, 150)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter your guess:", input_guess, 200)
frame.start()

# call new_game 
new_game()