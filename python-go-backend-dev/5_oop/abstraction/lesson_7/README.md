# Abstraction Practice
Let's work on a prototype card game that will eventually be added to Age of Dragons.

## Assignment
Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided for you as class variables. You won't need to modify them, but you will need to use them.

1. Complete the constructor:
    1. [ ] Initialize a private empty list called cards.
    2. [ ] Fill that empty list by calling the create_deck method within the constructor.

2. Complete the create_deck(self) method:
    1. [ ] Create a (Rank, Suit) tuple for each combination of the 52 cards in the deck and append them to the cards list.

> Order matters! The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

3. Complete the shuffle_deck(self) method:
    1. [ ] Use the random.shuffle() function (available from the random package) to shuffle the cards in the deck.
4. Complete the deal_card(self) method:
    1. [ ] .pop() the first card off the top of the deck (top of the deck is the end of the list) and return it. If there are no cards left in the deck the method should instead return None.