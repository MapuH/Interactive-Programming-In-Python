# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                
# define hand class
class Hand:
    def __init__(self):
        self.hand = list()

    def __str__(self):
        self.ans = ""
        for i in range(len(self.hand)):
            self.ans += str(self.hand[i]) + " "
        return "Hand contains %s" % (self.ans)

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        aces = False
        for card in self.hand:
            self.value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                aces = True
        if not aces:
            return self.value
        else:
            if self.value + 10 <= 21:
                return self.value + 10
            else:
                return self.value
   
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 82
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        return self.deck.pop(-1)
    
    def __str__(self):
        self.ans = ""
        for i in range(len(self.deck)):
            self.ans += str(self.deck[i]) + " "
        return "Deck contains %s" % (self.ans)

#define event handlers for buttons
def deal():
    global deck, player_hand, dealer_hand, message, outcome, score, in_play
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    outcome = ""
    message = "Hit or stand?"
    
    if in_play:
        score -= 1
        outcome = "You gave up last round"
    
    in_play = True

def hit():
    global deck, player_hand, message, outcome, score, in_play
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            score -= 1
            in_play = False
            outcome = "You have busted"
            message = "Deal again?"
       
def stand():
    global deck, dealer_hand, outcome, message, in_play, score
    if not in_play:
        message = "Deal again?"
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())            
        if dealer_hand.get_value() > 21:
            score += 1
            outcome = "You won, dealer went bust"
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                score -= 1
                outcome = "Dealer has %s and wins!" % (dealer_hand.get_value())
            else:
                score += 1
                outcome = "Dealer has %s, you win!" % (dealer_hand.get_value())
        message = "Deal again?"
        in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text('Blackjack', (180, 80), 56, 'Yellow')
    canvas.draw_text('Score: %s' % (score), (250, 150), 32, 'Black')
    canvas.draw_text('Dealer', (50, 200), 32, 'Black')
    canvas.draw_text(outcome, (200, 200), 32, 'Black')
    canvas.draw_text('Player: %s' % (player_hand.get_value()), (50, 375), 32, 'Black')
    canvas.draw_text(message, (200, 375), 32, 'Black')
    dealer_hand.draw(canvas, [50, 230])
    player_hand.draw(canvas, [50, 405])    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 230 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
# remember to review the gradic rubric