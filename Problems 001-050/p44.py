def pnum(n: int) -> int:
    return n * (3 * n - 1) // 2


def isPnum(p: int) -> bool:
    n = (1 + (1 + 24 * p) ** 0.5) / 6
    return n.is_integer()


def solve():
    pnums = [pnum(i) for i in range(100_01)]

    n = 1
    while True:
        for m in range(1, n):
            s, d = pnums[n] + pnums[m], pnums[n] - pnums[m]
            if isPnum(s) and isPnum(d):
                return d
        n += 1


print(solve())
