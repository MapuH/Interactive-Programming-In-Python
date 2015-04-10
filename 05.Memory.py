# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, open_cards, turns
    cards = range(8) * 2
    random.shuffle(cards)
    exposed = [False] * 16
    open_cards = list()
    turns = 0
    label.set_text('Turns = %s' % (turns))
     
# define event handlers
def mouseclick(pos):
    global exposed, state, open_cards, turns
    cardindex = pos[0] / 50
    
    #display the card, memorize it in a new list and increment turn
    if not exposed[cardindex]:
        exposed[cardindex] = True
        open_cards.append([cardindex, cards[cardindex]])
        if len(open_cards) == 2:
            turns += 1
            label.set_text('Turns = %s' % (turns))
        
    #check if cards match (used different logic than suggested in the instructions)
    if len(open_cards) > 2:
        if open_cards[0][1] != open_cards[1][1]:
            exposed[open_cards[0][0]] = False
            exposed[open_cards[1][0]] = False
            open_cards = [[cardindex, cards[cardindex]]]
        else:
            open_cards = [[cardindex, cards[cardindex]]]
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 10
    j = 0
    for card, h in zip(cards, range(16)):
        canvas.draw_text(str(card), [i, 70], 60, 'White')
        if exposed[h] == False:
            canvas.draw_polygon([[j, 0], [j+50, 0], [j+50, 100], [j, 100]], 2, 'Brown', 'Green')
        i += 50
        j += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
