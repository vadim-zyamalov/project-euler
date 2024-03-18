def limits(up_to: int) -> list[int]:
    res = [0]
    i = 0
    while True:
        nxt = res[-1] + (i + 1) * 9 * 10**i
        res.append(nxt)
        i += 1
        if nxt > up_to:
            break
    return res


def findDigit(pos, limits: list[int]) -> int:
    i = 1
    while limits[i] < pos:
        i += 1

    pos -= limits[i - 1] + 1
    num, d = divmod(pos, i)

    return int(str(10 ** (i - 1) + num)[d])


def solve(ns: list[int]) -> int:
    lims = limits(sorted(ns)[-1])
    res = 1
    for n in ns:
        res *= findDigit(n, lims)

    return res


print(solve([1, 10, 100, 1000, 10000, 100000, 1000000]))
