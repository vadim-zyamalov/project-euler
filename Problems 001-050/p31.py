from functools import cache
from time import time
import sys

sys.setrecursionlimit(10000)

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


@cache
def countCoins(num: int, last: int = 1) -> int:
    if num == 0:
        return 1
    return sum(
        countCoins(num - coin, coin)
        for coin in COINS
        if coin <= num and coin >= last
    )


def countFast(num: int) -> int:
    count = [0] * (num + 1)
    count[0] = 1

    for coin in COINS:
        for i in range(coin, num + 1):
            count[i] = count[i] + count[i - coin]

    return count[num]


t0 = time()
print(countCoins(200), time() - t0)
t0 = time()
print(countFast(200), time() - t0)
