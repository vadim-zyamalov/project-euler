from functools import cache


@cache
def power(n: int, p: int) -> int:
    assert n >= 0
    if p == 0:
        return 1
    if p % 2 == 0:
        x = power(n, p // 2)
        return x * x
    return n * power(n, p - 1)


def sumDigits(num: int) -> int:
    res = 0
    while num:
        num, d = divmod(num, 10)
        res += d
    return res


print(sumDigits(power(2, 1_000)))
