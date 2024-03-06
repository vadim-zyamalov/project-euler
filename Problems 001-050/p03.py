from math import sqrt
from utils import primesTo

NUM = 600_851_475_143


def solve(num: int) -> int:
    primes = primesTo(int(sqrt(num)))
    idx = 0

    while True:
        if primes[idx] == num:
            return num
        if num % primes[idx] == 0:
            num //= primes[idx]
            idx = 0
        else:
            idx += 1


print(solve(NUM))
