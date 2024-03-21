from utils import primesTo, isPrime
from math import log10
from functools import cache
from time import time


PRIMES = primesTo(1_000_000)


def isTractable(num: int) -> bool:
    nL = nR = num
    _n = int(log10(nL))

    while nL and nR:
        if nL not in PRIMES or nR not in PRIMES:
            return False

        nL %= 10**_n
        nR //= 10
        _n -= 1

    if nL or nR:
        return False

    return True


def solve():
    res = [p for p in PRIMES[8:] if isTractable(p)]
    return res


def rightTractable() -> list[int]:
    numbers = [[2, 3, 5, 7]]  # на эти цифры может начинаться число
    n = 0
    while True:
        numbers.append([])
        for j in numbers[n]:
            for nd in [1, 3, 7, 9]:  # эти цифры могут быть в хвосте числа
                nxt = 10 * j + nd
                if isPrime(nxt):
                    numbers[n + 1].append(nxt)
        if numbers[n + 1] == []:
            break
        n += 1
    return [el for lst in numbers[1:] for el in lst]


def isLeftTructable(num: int) -> bool:
    n = int(log10(num))
    num %= 10**n
    while num:
        if not isPrime(num):
            return False
        n -= 1
        num %= 10**n
    return True


def solve_forum() -> list[int]:
    return [p for p in rightTractable() if isLeftTructable(p)]


t0 = time()
print(sum(solve()), f"{time()-t0:.3f}")
t0 = time()
print(sum(solve_forum()), f"{time()-t0:.3f}")
