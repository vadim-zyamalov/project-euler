from itertools import (
    permutations as perms,
    combinations_with_replacement as rcombs,
    combinations as combs,
)
from utils import listToNum, isPrime


def findSeq(nums: list[int], proh=1487) -> tuple[int, int, int]:
    for i, j, k in combs(nums, r=3):
        if i == proh:
            continue
        if k - j == j - i:
            return i, j, k
    return (0, 0, 0)


def checkComb(comb: tuple[int, ...]) -> tuple[int, int, int]:
    primes = set(listToNum(p) for p in perms(comb) if p[0] != 0)
    primes = list(p for p in primes if isPrime(p))
    if len(primes) < 3:
        return (0, 0, 0)
    return findSeq(primes)


def solve():
    for digits in rcombs(range(10), r=4):
        if all(d & 1 == 0 for d in digits):
            continue
        x, y, z = checkComb(digits)
        if x == 0:
            continue
        return str(x) + str(y) + str(z)


print(solve())
