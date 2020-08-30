'''
This is the 2nd milestone project from the online Udemy Python course. A basic BlackJack game is simulated. 
'''
import random

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

player_done = False

class Card:

    def __init__(self, suit, rank):
       self.suit = suit
       self.rank = rank
       self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __str__(self):
        return f'Deck has {len(self.cards)} cards'


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

    def adjust_ace(self):
        pass


class Chip:

    def __init__(self):
        self.chips = 100
        self.bet = 0

    def win_bet(self):
        self.chips += self.bet

    def lose_bet(self):
        self.chips -= self.bet



class Player:

    def __init__(self, name):
        self.name = name
        self.chip = Chip()
        self.hand = Hand()


def show_partial_cards(dealer_hand, player_hand):

    print('Dealer cards:')

    for card in dealer_hand.cards:

        if card == dealer_hand.cards[0]:
            print('\t*** Hidden ***')
        else:
            print(f'\t{card}')

    print(f'\nPlayer count {player_hand.value} from cards:')
    for card in player_hand.cards:
        print(f'\t{card}')


def show_all_cards():
    pass


def take_bets(player):
    # Place bet
    while True:
        try:
            bet = int(input('Place number of chips for your bet: '))
        except:
            print('Ooops, please enter a valid number')
            continue
        else:
            if bet > player.chip.chips:
                print('Insufficient chips!')
                continue
            else:
                player.chip.bet = bet
                break


def hit(deck, player_hand):
    player_hand.add_card(deck.deal())
    player_hand.adjust_ace()
    

def hit_or_stand(deck, player_hand):
    global player_done

    while True:
        action = input('\nHit or Stand? (enter h or s): ')

        if action.lower() == 'h':
            hit(deck, player_hand)
        elif action.lower() == 's':
            player_done = True
            print('Player stands, Dealer is playing')
        else:
            print('Invalid input, please try again.')
            continue
        break

''' 
Main game logic
'''
# Global variables
dealer = Player('Dealer')
player = Player('Player')
deck = Deck() 

# game_count = 0
# game_on = True

deck.shuffle()

#while game_on = True:

take_bets(player)

player.hand.add_card(deck.deal())  # deal Player's first card
dealer.hand.add_card(deck.deal())  # deal Dealer's first card
player.hand.add_card(deck.deal())  # deal Player's second card
dealer.hand.add_card(deck.deal())  # deal Dealer's second card

show_partial_cards(dealer.hand, player.hand)

while player_done == False:
    hit_or_stand(deck, player.hand)
    show_partial_cards(dealer.hand, player.hand)

'''
Unit Tests
'''
'''
# Test card initialisation
print('\n--- 1. INIT CARD ---')
ace_of_hearts = Card('Heart','Ace')
print(ace_of_hearts.suit)
print(ace_of_hearts)

# Test deck initialisation
print('--- 2. INIT DECK ---')
deck = Deck()
print(deck)
print(deck.cards[0])
print(deck.cards[-1])
deck.shuffle()
print('-Deck shuffled-')
print(deck.cards[0])
print(deck.cards[-1])
print('-Drawn 2 cards-')
deck.deal()
deck.deal()
print(deck)

# Test player initialisation
print('--- 3. INIT PLAYER & HAND ---')
test_player = Player('Test Player')
print(test_player.name)
print(test_player.hand.value) 
'''