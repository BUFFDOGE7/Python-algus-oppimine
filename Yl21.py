import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            value += card.get_value()
            if card.rank == 'Ace':
                aces += 1
        
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    def display(self, hide_first=False):
        if hide_first:
            print("  [Hidden]")
            for card in self.cards[1:]:
                print(f"  {card}")
        else:
            for card in self.cards:
                print(f"  {card}")
            print(f"  Total: {self.get_value()}")

def play_blackjack():
    print("=" * 40)
    print("Welcome to Blackjack!")
    print("=" * 40)

    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    print("\nDealer's Hand:")
    dealer_hand.display(hide_first=True)
    
    print("\nYour Hand:")
    player_hand.display()
    
    if player_hand.get_value() == 21:
        print("\nBlackjack! You win!")
        return
    
    while True:
        choice = input("\nWould you like to (h)it or (s)tand? ").lower()
        
        if choice == 'h':
            player_hand.add_card(deck.deal())
            print("\nYour Hand:")
            player_hand.display()
            
            if player_hand.get_value() > 21:
                print("\nBust! You lose!")
                return
            elif player_hand.get_value() == 21:
                break
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please enter 'h' or 's'.")
    
    print("\nDealer's turn...")
    print("\nDealer's Hand:")
    dealer_hand.display()
    
    while dealer_hand.get_value() < 17:
        print("\nDealer hits...")
        dealer_hand.add_card(deck.deal())
        dealer_hand.display()
    
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    
    print("\n" + "=" * 40)
    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value:
        print(f"You win! {player_value} vs {dealer_value}")
    elif player_value < dealer_value:
        print(f"Dealer wins! {dealer_value} vs {player_value}")
    else:
        print(f"Push! Both have {player_value}")
    print("=" * 40)

def main():
    while True:
        play_blackjack()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()