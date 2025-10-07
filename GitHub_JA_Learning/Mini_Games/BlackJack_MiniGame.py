import random

# -------------------------------
# Card class: represents a single playing card
# -------------------------------


class Card:
    def __init__(self, suit, rank):
        """
        suit: string ("hearts", "spades", etc.)
        rank: dict with "rank" (e.g., 'A', '2', 'J') and "value" (int)
        """
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        # Display format: "A of hearts"
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        """Initialize a deck of 52 cards (13 ranks × 4 suits)."""
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [{"rank": "A", "value": 11},
                {"rank": "2", "value": 2}, 
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10}
                ]
        
        # Generate full deck
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
            
    def shuffle(self):
        """Shuffle the deck if there are at least 2 cards left."""
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        
        
    def deal(self, number):
        """
        Deal a given number of cards from the deck.
        Returns a list of Card objects.
        """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
    
# -------------------------------
# Hand class: represents cards held by a player or dealer
# -------------------------------

class Hand:
    def __init__(self, dealer = False):
        """
        dealer: True if this hand belongs to the dealer.
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        """Add one or more cards to the hand."""
        self.cards.extend(card_list)
        
    def calculate_value(self):
        #   """Recalculate the total value of the hand, handling Aces."""
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
                
        # Adjust Ace from 11 to 1 if total > 21        
        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        """Return the hand's current value."""
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        """Return True if the hand is exactly 21."""
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards = False):
        """
        Print the hand's cards. Dealer's first card is hidden by default.
        show_all_dealer_cards=True reveals all dealer cards.
        """
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards \
            and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value: ", self.get_value())
        print()

# -------------------------------
# Game class: main Blackjack game loop
# -------------------------------
        
class Game:
    def play(self):
        """Main game loop. Runs multiple Blackjack games as requested."""
        game_number = 0
        games_to_play = 0
        
        # Ask how many games to play
        while games_to_play <=0:
            try: 
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number to play.")

        while game_number < games_to_play:
            game_number += 1
            
            # New shuffled deck each game
            deck = Deck()
            deck.shuffle()
            
            # Initialize player and dealer hands
            player_hand = Hand()
            dealer_hand = Hand(dealer = True)
            
            # Deal 2 cards each
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
                
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            # Player turn: hit or stand
            choice =""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue
            
             # Dealer turn: must hit until value >= 17
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
                
            dealer_hand.display(show_all_dealer_cards = True)
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            # Compare final results
            print("Final Results")
            print("Your Hand: ", player_hand_value)
            print("Dealers Hand: ", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, True)
        
        print("\n Thanks for playing! ")
                    
        
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """
        Determine winner based on Blackjack rules.
        If game_over=False, check for busts/blackjacks during play.
        If game_over=True, compare final values.
        """
        if not game_over:
            if player_hand.get_value() > 21:
                print(" You Busted! Dealer is the WINNER!!!")
                return True
            elif dealer_hand.get_value() > 21:
                print(" Dealer Busted! YOU ARE THE WINNER!!!! :D ")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print(" Both Players have BLACKJACK! ITS A TIE! oh my.......... ")
                return True
            elif player_hand.is_blackjack():
                print(" You have blackjack! YOU WIN!  ")
                return True
            elif dealer_hand.is_blackjack():
                print(" Dealer has blackjack! Dealer Wins!")
                return True

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win!!! ")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("TIE!!! ")
            else: 
                print("Dealer WINS ")
            return True
        return False

g = Game()
g.play()





## Method 1 for Shuffle cards to produce 2 cards. 
#cards_dealt = deal(2)
#card = cards_dealt[0]
#rank = card[1]

#if rank == "A":
#    value = 11
#elif rank == "J" or rank == "Q" or rank == "K":
#    value = 10
#else:
#    value = rank
#rank_dict = {"rank": rank, "value": value}

#print(rank_dict["rank"], rank_dict["value"])