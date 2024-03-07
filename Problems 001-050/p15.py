from functools import cache
from math import factorial


@cache
def count(x: int, y: int, lim: int) -> int:
    if x < 0 or y < 0:
        return 0
    if (x, y) == (0, 0):
        return 1
    return count(x - 1, y, lim) + count(x, y - 1, lim)


def countComb(n, m):
    return factorial(n + m) // (factorial(n) * factorial(m))


print(count(20, 20, 20))
print(countComb(20, 20))
