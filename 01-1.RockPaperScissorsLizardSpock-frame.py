import simplegui
import random

# Define global variables
weapons = ('rock', 'Spock', 'paper', 'lizard', 'scissors')
plr_choice = None
comp_choice = None
plr_points = 0
comp_points = 0
rounds = 0

# Welcome message and rules
print """Welcome to rock - paper - scissors - lizard - Spock!
The rules are simple:\n
1. Scissors cuts Paper
2. Paper covers Rock
3. Rock crushes Lizard
4. Lizard poisons Spock
5. Spock smashes Scissors
6. Scissors decapitates Lizard
7. Lizard eats Paper
8. Paper disproves Spock
9. Spock vaporizes Rock
10. Rock crushes Scissors\n
Play against the computer.
First one to make 5 points wins the round!\n"""

# Start a new round
def new_round():
    global plr_points, comp_points, rounds
    plr_points = 0
    comp_points = 0
    rounds += 1
    print "ROUND", rounds

# Main game function
def rspls():
    global comp_choice, plr_points, comp_points
    comp_choice = random.randrange(5)
    print "You choose", weapons[plr_choice]
    print "Computer chooses", weapons[comp_choice]
    
    # Check who wins
    result = (plr_choice - comp_choice) % 5
    if result == 0:
        print "Oh, it's a tie!"
    elif result == 1 or result == 2:
        plr_points += 1
        print "You win!"
    else:
        comp_points +=1
        print "Computer wins!"
    
    # Current points
    print "Player: %s, Computer: %s\n" % (plr_points, comp_points)
    
    # Check who won the round
    if plr_points == 5:
        print "Congratulations, you won this round!\n"
        new_round()
    elif comp_points == 5:
        print "Sorry, computer won this round, better luck next time.\n"
        new_round()

# Define handlers for the buttons
def rock():
    global plr_choice
    plr_choice = 0
    rspls()

def spock():
    global plr_choice
    plr_choice = 1
    rspls()

def paper():
    global plr_choice
    plr_choice = 2
    rspls()

def lizard():
    global plr_choice
    plr_choice = 3
    rspls()

def scissors():
    global plr_choice
    plr_choice = 4
    rspls()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Rock-Paper-Scissors-Lizard-Spock", 200, 200)
frame.add_label("Choose your weapon:")
frame.add_button("Rock", rock, 100)
frame.add_button("Paper", paper, 100)
frame.add_button("Scissors", scissors, 100)
frame.add_button("Lizard", lizard, 100)
frame.add_button("Spock", spock, 100)
frame.start()

# Call 1st round when the game starts
new_round()
