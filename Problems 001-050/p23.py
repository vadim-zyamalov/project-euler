from utils import factor


def sumDivisors(num: int) -> int:
    factors = factor(num)

    res = 1
    for p, a in factors.items():
        res *= (p ** (a + 1) - 1) // (p - 1)

    return res - num


def abundant(limit: int) -> list[int]:
    res = []
    for i in range(2, limit):
        if sumDivisors(i) > i:
            res.append(i)
    return res


def solve(limit: int) -> int:
    # Skipping 1 and 2
    anums = abundant(limit)
    tmp = [True] * limit
    for i in range(len(anums)):
        for j in range(i, len(anums)):
            if (s := anums[i] + anums[j]) < limit:
                tmp[s - 1] = False
    return sum(i for i in range(1, limit) if tmp[i - 1])


print(solve(28_123))
