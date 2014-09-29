#! /usr/bin/python
from collections import Counter

RANKS = "23456789TJQKA"
SUITS = "CDHS"


class PokerHand(object):
    def __init__(self, cards):
        #cards is a list of cards as strings,
        #e.g. ['AS', 'KD', '3D', 'JD', '8H']
        tmp = []
        for card in cards:
            rank = RANKS.index(card[0])
            suit = SUITS.index(card[1])
            val = rank * 4 + suit
            tmp.append((val, rank, suit, card))

        self.vals, self.ranks, self.suits, self.cards = [], [], [], []
        for val, rank, suit, card in sorted(tmp):
            self.vals.append(val)
            self.ranks.append(rank)
            self.suits.append(suit)
            self.cards.append(card)

        self.counts = sorted(Counter(self.ranks).most_common(),
                             reverse=True,
                             key=lambda x: (x[1], x[0]))

    def __str__(self):
        return " ".join(self.cards)

    def is_straight(self):
        for i in range(1, 5):
            if self.ranks[i] - self.ranks[i - 1] != 1:
                return False
        return True

    def is_flush(self):
        return len(set(self.suits)) == 1

    def minor_score(self):
        return "".join("%02d" % r for r, c in self.counts)

    def major_score(self):
        cnt_score = 1
        if self.counts[0][1] == 4:
            cnt_score = 8  # four kind
        elif self.counts[0][1] == 3:
            cnt_score = 4  # triple
            if self.counts[1][1] == 2:
                cnt_score = 7  # full house
        elif self.counts[0][1] == 2:
            cnt_score = 2  # pair
            if self.counts[1][1] == 2:
                cnt_score = 3  # 2 pair
        straight_score = 5 if self.is_straight() else 0
        flush_score = 6 if self.is_flush() else 0
        return max(straight_score, flush_score, cnt_score)

    @property
    def score(self):
        return float("%s.%s" % (self.major_score(), self.minor_score()))


if __name__ == "__main__":
    ret = 0
    with open("poker.txt", "rU") as fp:
        for line in fp.read().splitlines():
            cards = line.split()
            hand1 = PokerHand(cards[:5])
            hand2 = PokerHand(cards[5:])

            ret += hand1.score > hand2.score

    print ret
