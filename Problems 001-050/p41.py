from itertools import permutations
from utils import isPrime


def solve() -> int:
    # Я понял, что nd == {2, 3} можно не рассматривать,
    # но не раскрутил это для nd == {5, 6, 8, 9} :)
    for nd in [7, 4]:
        for pl in permutations(range(nd, 0, -1)):
            # Четные числа рассматривать смысла нет
            if pl[-1] & 1 == 0:
                continue
            p = 0
            for d in pl:
                p = p * 10 + d
            if isPrime(p):
                return p
    return -1


print(solve())
