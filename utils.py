from functools import cache
from math import floor, log, sqrt
from collections import defaultdict


def primesTo(num):
    result = [2]

    if num == 2:
        return result

    marked = [False] * (num // 2)

    for p in range(3, num + 1, 2):
        if marked[(p - 3) // 2]:
            continue
        result += [p]
        for mul in range(p**2, num, 2 * p):
            marked[(mul - 3) // 2] = True

    return result


def primeLim(n: int) -> int:
    return int(n * log(n) + n * log(log(n)))


def factor(num: int) -> defaultdict:
    assert num > 1, "1 is not a prime number"
    assert isinstance(num, int), "num should be integer"

    factors = defaultdict(int)

    _num = num
    primes = primesTo(num)

    for p in primes:
        if p > _num:
            break
        while _num % p == 0:
            factors[p] += 1
            _num //= p

    if len(factors) == 0:
        factors[num] = 1

    return factors


def gcd(x: int, y: int) -> int:
    if abs(x) < abs(y):
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


def gcdL(xs: list[int]) -> int:
    x = xs[0]

    for y in xs[1:]:
        x = gcd(x, y)

    return x


def lcm(x: int, y: int) -> int:
    return abs(x * y) // gcd(x, y)


def lcmL(xs: list[int]) -> int:
    x = xs[0]

    for y in xs[1:]:
        x = lcm(x, y)

    return x


def numToList(num: int) -> list[int]:
    res = []
    while num:
        num, q = divmod(num, 10)
        res += [q]
    return res[::-1]


@cache
def fact(n: int) -> int:
    assert n >= 0
    assert isinstance(n, int)

    if n == 0:
        return 1
    return n * fact(n - 1)
