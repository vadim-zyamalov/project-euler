from functools import cache


@cache
def collatzLen(n: int) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return collatzLen(n // 2) + 1
    return collatzLen((3 * n + 1) // 2) + 2


def solve(limit: int) -> int:
    maxl = 1
    maxi = 1

    for i in range(limit // 2, limit):
        if collatzLen(i) > maxl:
            maxl = collatzLen(i)
            maxi = i

    return maxi


print(solve(1_000_000))
