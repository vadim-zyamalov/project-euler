from functools import cache
from math import sqrt, prod
from utils import primesTo, factor
from collections import defaultdict


@cache
def trNum(n: int) -> int:
    if n == 1:
        return 1
    return n + trNum(n - 1)


def solve(limit: int) -> int:
    i = 2
    while True:
        num = trNum(i)
        factors = factor(num)
        if prod(map(lambda x: x + 1, factors.values())) >= limit:
            return num
        i += 1


print(solve(500))
