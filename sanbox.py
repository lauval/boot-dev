import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]

# cards = [(suit, rank) for suit in SUITS for rank in RANKS]

cards = []

# test
for suit in SUITS:
    for rank in RANKS:
        cards.append((suit, rank))

print(len(cards))
print(cards)

print("\n Now shuffling")
random.shuffle(cards)
print(cards)

print("Dealing from the top of the deck")
top_of_deck = cards.pop()
print(top_of_deck)
