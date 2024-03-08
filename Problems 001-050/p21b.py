# https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors

from utils import factor


def sumDivisors(num: int) -> int:
    factors = factor(num)

    res = 1
    for p, a in factors.items():
        res *= (p ** (a + 1) - 1) // (p - 1)

    return res - num


def amicable(limit: int) -> list[tuple[int, int]]:
    res = []

    for i in range(2, limit):
        j = sumDivisors(i)
        if j > i:
            if sumDivisors(j) == i:
                res.append((i, j))

    return res


print(sum(el for p in amicable(10000) for el in p))
