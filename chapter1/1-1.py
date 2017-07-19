import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def test_seq():
    fd = FrenchDeck()

    print fd[0]
    print len(fd)
    print choice(fd)

    print fd[:3]

    for card in fd:
        print card

    for card in reversed(fd):
        print car

def test_sort():
    suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)
    def cmp(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        ret = rank_value * len(suit_values) + suit_values[card.suit]
        return ret

    fd = FrenchDeck()
    for card in sorted(fd, key=cmp):
        print card

test_sort()
