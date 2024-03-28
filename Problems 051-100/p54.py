from typing import LiteralString, Sequence


ORDER = {v: k for k, v in enumerate("23456789TJQKA")}
STRAIGHTS = ["AKQJT98765432"[i : i + 5] for i in range(13 - 4)]


class Hand:
    def __init__(self, hand: Sequence[str]) -> None:
        self.hand = sorted(hand, key=lambda cs: ORDER[cs[0]], reverse=True)
        self.strength, self.rank = self.type()

    def type(self) -> tuple[int, list[tuple[int, int]]]:
        strength = 0
        cards_c = {}
        cards = ""
        suits_c = {}

        for cs in self.hand:
            c, s = list(cs)
            if c not in cards_c:
                cards_c[c] = 0
            cards_c[c] += 1
            cards += c
            if s not in suits_c:
                suits_c[s] = 0
            suits_c[s] += 1

        if len(suits_c) == 1:
            if cards in STRAIGHTS:
                strength = 9 if STRAIGHTS.index(cards) == 0 else 8
            else:
                strength = 5

        match len(cards_c):
            case 2:
                strength = max(strength, 7 if 4 in cards_c.values() else 6)
            case 3:
                strength = max(strength, 3 if 3 in cards_c.values() else 2)
            case 4:
                strength = max(strength, 1)
            case 5:
                if cards in STRAIGHTS:
                    strength = max(strength, 4)

        cards_c = [(v, ORDER[k]) for k, v in cards_c.items()]
        cards_c.sort(reverse=True)

        return strength, cards_c

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        if self.strength < other.strength:
            return False
        return self.rank > other.rank

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        if self.strength > other.strength:
            return False
        return self.rank < other.rank

    def __eq__(self, other):
        return (not (self > other)) and (not (self < other))


with open("0054_poker.txt", "r") as f:
    res = 0
    for line in f:
        line = line.strip()
        if line == "":
            break
        cs = line.strip().split()
        res += Hand(cs[:5]) > Hand(cs[5:])

print(res)
