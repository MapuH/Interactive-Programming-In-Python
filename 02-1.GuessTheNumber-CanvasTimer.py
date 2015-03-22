import simplegui
import random

# initialize global variables
num_range = 100
num_of_guesses = 7

# variables used with the timers
time = 90
result_time = 0
ngstart = 6

# messages printed on the canvas
range_msg = ""
guess_msg = ""
direction_msg = ""
remaining_msg = ""
result_msg = ""
game_over_msg = ""
new_game_msg = ""

# helper function to format timer
def format(t):
    minutes = t / 60
    seconds = t % 60
    return "Time %s:%02d" % (minutes, seconds)

# helper function to start and restart the game
def new_game():
    global secret_number, num_of_guesses
    global range_msg, guess_msg, direction_msg, remaining_msg, result_msg, game_over_msg, new_game_msg
    global time, result_time, ngstart
    
    # reset messages
    guess_msg = ""
    direction_msg = ""
    remaining_msg = ""
    result_msg = ""
    game_over_msg = ""
    new_game_msg = ""
    
    # reset timers
    timer.stop()
    ngtimer.stop()
    result_time = 0
    ngstart = 6
    
    #reset secret number and range
    secret_number = random.randrange(num_range)
    if num_range == 100:
        num_of_guesses = 7
        range_msg = "Range is 0 to 100, you're allowed %s guesses" % (num_of_guesses)
        time = 90
    else:
        num_of_guesses = 10
        range_msg = "Range is 0 to 1000, you're allowed %s guesses" % (num_of_guesses)
        time = 120

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
    global num_of_guesses, guess_msg, direction_msg, remaining_msg, result_msg
    int_guess = int(guess)
    guess_msg = "You guessed %s" % (int_guess)
    timer.start()

    if secret_number > int_guess:
        num_of_guesses -= 1
        direction_msg = "Higher"
        remaining_msg = "%s guesses remaining" % (num_of_guesses)
    elif secret_number < int_guess:
        num_of_guesses -= 1
        direction_msg = "Lower"
        remaining_msg = "%s guesses remaining" % (num_of_guesses)
    else:
        result_msg = "Well done! You guessed it in %s seconds" % (result_time)
        direction_msg = ""
        remaining_msg = ""
        timer.stop()
        ngtimer.start()
    
    if num_of_guesses == 0:
        result_msg = "Sorry, you did not guess the number, it was %s" % (secret_number)
        ngtimer.start()
                

# timers handlers
def countdown():
    global time, result_time, result_msg
    time -= 1
    result_time += 1
    if time <= 0:
        timer.stop()
        result_msg = "Sorry, you ran out of time!"
        ngtimer.start()
    
def new_game_timer():
    global ngstart, game_over_msg, new_game_msg
    ngstart -= 1
    game_over_msg = "G A M E  O V E R"
    new_game_msg = " New game will start in %s seconds" % (ngstart)
    if ngstart <= 0:
        new_game()

def draw(canvas):
    # draw title
    canvas.draw_text("====== Guess The Number ======", (50, 80), 36, "Silver")
    canvas.draw_polygon(((20, 20), (620, 20), (620, 120), (20, 120)), 6, "Silver")
    
    #draw timer
    canvas.draw_text(format(time), (530, 160), 22, "Silver")
    
    # draw messages
    canvas.draw_text(range_msg, (20, 160), 22, "Silver")
    canvas.draw_text(guess_msg, (20, 210), 22, "Silver")
    canvas.draw_text(direction_msg, (20, 240), 22, "Silver")
    canvas.draw_text(remaining_msg, (20, 270), 22, "Silver")
    canvas.draw_text(result_msg, (20, 300), 22, "Silver")
    canvas.draw_text(game_over_msg, (210, 380), 26, "Silver")
    canvas.draw_text(new_game_msg, (160, 440), 22, "Silver")
    
# create frame
frame = simplegui.create_frame("Guess the number", 640, 480)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter your guess:", input_guess, 200)
frame.set_draw_handler(draw)

# create timers
timer = simplegui.create_timer(1000, countdown)
ngtimer = simplegui.create_timer(1000, new_game_timer)


# start the frame and call new_game
frame.start()
new_game()
