from functools import cache
from math import log
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

    # Factor 2
    while _num % 2 == 0:
        factors[2] += 1
        _num //= 2

    p = 3
    while p * p <= _num:
        while _num % p == 0:
            factors[p] += 1
            _num //= p
        p += 2

    if _num > 1:
        factors[_num] += 1

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


@cache
def fib1(n: int) -> int:
    assert isinstance(n, int)
    assert n > 0

    if n < 3:
        return 1
    return fib1(n - 1) + fib1(n - 2)


@cache
def fib(n: int) -> int:
    assert isinstance(n, int)
    assert n >= 0

    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
