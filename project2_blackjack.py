'''
This is a basic text-based BlackJack game. There is only 1 Player, playing against a computer Dealer. 
The only action that a Player can take in the game is Hit or Stand. This game goes not include other common actions such as Split, Double Down or Insurance.  
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
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def clear(self):
        self.cards = []
        self.value = 0
        self.aces = 0


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

    print('\nDealer cards:')

    for card in dealer_hand.cards:

        if card == dealer_hand.cards[0]:
            print('\t*** Hidden ***')
        else:
            print(f'\t{card}')

    print(f'\nPlayer count {player_hand.value} from cards:')
    for card in player_hand.cards:
        print(f'\t{card}')


def show_all_cards(dealer_hand, player_hand):
    print(f'\nDealer count {dealer_hand.value} from cards:')
    for card in dealer_hand.cards:
        print(f'\t{card}')

    print(f'\nPlayer count {player_hand.value} from cards:')
    for card in player_hand.cards:
        print(f'\t{card}')


def take_bets(player):
    # Place bet
    while True:
        try:
            bet = int(input(f'\n>> You have {player.chip.chips} chips. Place number of chips for your bet: '))
        except:
            print('>> Ooops, please enter a valid number')
            continue
        else:
            if bet > player.chip.chips:
                print('>> Insufficient chips!')
                continue
            else:
                player.chip.bet = bet
                break


def hit(deck, player_hand):

    if len(deck.cards) == 0:
        deck = new_deck()

    player_hand.add_card(deck.deal())
    player_hand.adjust_ace()
    

def hit_or_stand(deck, player_hand):
    global player_done

    while True:
        action = input('\n>> Hit or Stand? (enter h or s): ')

        if action.lower() == 'h':
            hit(deck, player_hand)
        elif action.lower() == 's':
            player_done = True
            print('>> Player stands, Dealer is playing...')
        elif action.lower() == 'exit':
            exit()
        else:
            print('>> Invalid input, please try again.')
            continue
        break


def new_deck():
    deck = Deck()
    deck.shuffle()
    print('\n>> No more cards on deck, new deck added and shuffled.')
    print(deck)
    return deck

def player_win(player):
    player.chip.win_bet()

def player_lose(player):
    player.chip.lose_bet()

def player_blackjack(player):
    player.chip.bet *= 2
    player.chip.win_bet()


''' 
Main game logic
'''

dealer = Player('Dealer')
player = Player('Player')
deck = Deck() 

deck.shuffle()

print('Welcome to BlackJack!')


while True:

    # clear hands for a new round and reset flag
    dealer.hand.clear()
    player.hand.clear()
    player_done = False
    dealer_to_play = True

    # take bet from Player
    take_bets(player)

    # add new deck if not enough cards to deal
    if len(deck.cards) < 4:
        deck = new_deck()

    # deal first 2 cards for Dealer and Player
    player.hand.add_card(deck.deal())  # deal Player's first card
    dealer.hand.add_card(deck.deal())  # deal Dealer's first card
    player.hand.add_card(deck.deal())  # deal Player's second card
    dealer.hand.add_card(deck.deal())  # deal Dealer's second card     

    while player_done == False:
        
        # check for BlackJack 
        if len(player.hand.cards) == 2 and player.hand.value == 21 and dealer.hand.value != 21:
            show_all_cards(dealer.hand, player.hand)
            player_blackjack(player)
            print('>> BlackJack!! Player wins double the bet!')
            dealer_to_play = False
            break
        elif len(player.hand.cards) == 2 and player.hand.value == 21 and dealer.hand.value == 21:
            show_all_cards(dealer.hand, player.hand)
            print('>> Both Player and Dealer has BlackJack. Push!')
            dealer_to_play = False
            break
        
        show_partial_cards(dealer.hand, player.hand)

        # Player choose to hit or stand
        hit_or_stand(deck, player.hand)

        # Player loses immediately if busts
        if player.hand.value > 21:
            show_all_cards(dealer.hand, player.hand)
            player_lose(player)
            print('>> Player busts, Dealer wins')
            dealer_to_play = False
            break
        elif player.hand.value == 21:
            print('>> You have a total of 21! Dealer is playing...')
            break
            
    # Dealer's turn    
    if dealer_to_play == True:

        while dealer.hand.value < 17:
            hit(deck, dealer.hand)

        show_all_cards(dealer.hand, player.hand)

        if dealer.hand.value > 21: # Dealer bust
            player_win(player)
            print('>> Dealer busts! Player wins!\n')

        elif dealer.hand.value > player.hand.value: # Dealer wins
            player_lose(player)
            print('>> Dealer wins\n')

        elif dealer.hand.value < player.hand.value: # Player wins
            player_win(player)
            print('>> Player wins!\n')

        elif dealer.hand.value == player.hand.value: # Push
            print('>> Push!\n')
