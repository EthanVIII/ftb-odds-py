from enum import Enum, auto

class Suit(Enum):
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()
    CLUBS = auto()
    def __str__(self):
        if self == Suit.DIAMONDS:
            return "DIAMONDS"
        if self == Suit.HEARTS:
            return "HEARTS"
        if self == Suit.SPADES:
            return "SPADES"
        if self == Suit.CLUBS:
            return "CLUBS"

def suit_str_to_suit(suit_str):
    if suit_str == 'D':
        return Suit.DIAMONDS
    if suit_str == 'H':
        return Suit.HEARTS
    if suit_str == 'S':
        return Suit.SPADES
    if suit_str == 'C':
        return Suit.CLUBS
    else:
        assert False, "Invalid Suit"

class Color(Enum):
    RED = auto()
    BLACK = auto()

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    def __str__(self):
        return str(self.val) + str(self.suit)[0]
 
def suit_to_col(suit):
    if suit == Suit.DIAMONDS or suit == Suit.HEARTS:
        return Color.RED
    if suit == Suit.SPADES or suit == Suit.CLUBS:
        return Color.BLACK

def is_valid_card_string(card_string):
    if len(card_string) != 3 and len(card_string) != 2:
        return False
    if card_string[-1] not in ['D','H','S','C']:
        return False
    if int(card_string[0:len(card_string)-1]) < 0 or int(card_string[0:len(card_string)-1]) > 13:
        return False
    return True

def process_new_card(card_string):
    suit = suit_str_to_suit(card_string[-1])
    val = int(card_string[0:len(card_string)-1])
    return Card(suit, val)

def next_colour_odds(seen_cards):
    red_cards = 26
    black_cards = 26
    for card in seen_cards:
        if suit_to_col(card.suit) == Color.RED:
            red_cards = red_cards -1
        elif suit_to_col(card.suit) == Color.BLACK:
            black_cards = black_cards -1
    total = red_cards + black_cards
    return 'RED: '+str(round(red_cards/total,4))+'; BLACK:'+str(round(black_cards/total,4))

# Excluding the exact card for both.
def higher_lower_odds(seen_cards):
    latest_card = seen_cards[-1]
    higher_odds = 13 - latest_card.val
    lower_odds = latest_card.val - 1
    return 'HIGHER: ' + str(round(higher_odds/12,4)) + '; LOWER: ' + str(round(lower_odds/12,4))

# Inclusive of cards at set boundaries.
def in_between_odds(seen_cards):
    if len(seen_cards) < 2:
        return 'NA'
    first_val = seen_cards[-1].val
    second_val = seen_cards[-2].val
    return str( round( ((abs(first_val - second_val) + 1)/13), 4 ) )
    
def next_suit_odds(seen_cards):
    diamonds = hearts = clubs = spades = 13
    for card in seen_cards:
        if card.suit == Suit.DIAMONDS:
            diamonds -= 1
        elif card.suit == Suit.HEARTS:
            hearts -= 1
        elif card.suit == Suit.CLUBS:
            clubs -= 1
        elif card.suit == Suit.SPADES:
            spades -= 1
    total = 52 - len(seen_cards)
    diamond_odds = round(diamonds/total, 4)
    hearts_odds  = round(hearts  /total, 4)
    clubs_odds   = round(clubs   /total, 4)
    spades_odds  = round(spades  /total,4)
    return 'D: ' + str(diamond_odds) + '; H: ' + str(hearts_odds) + '; C: ' + str(clubs_odds) + '; S: ' + str(spades_odds)


def main():
    from enum import Enum
    seen_cards = []
    while True:
        x = input(': ')
        if x == 'q':
            print('Exiting odds calculator...')
            break
        elif x == 'r':
            print('Resetting played cards...')
            seen_cards = []
        elif is_valid_card_string(x):
            card = process_new_card(x)
            seen_cards.append(card)
            print('Next Colour Odds:                  ' + next_colour_odds(seen_cards))
            print('Next Card Higher/Lower Odds:       ' + higher_lower_odds(seen_cards))
            print('Next Card (In) between the last 2: ' + in_between_odds(seen_cards))
            print('Next Suit Odds:                    ' + next_suit_odds(seen_cards))
        else:
            print('Invalid card/command')

if __name__ == "__main__":
    main()
