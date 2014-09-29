from poker import PokerHand


def euler54():
    ret = 0
    with open("poker54.txt", "rU") as fp:
        for line in fp.read().splitlines():
            cards = line.split()
            hand1 = PokerHand(cards[:5])
            hand2 = PokerHand(cards[5:])
            ret += hand1.score > hand2.score
    return ret
