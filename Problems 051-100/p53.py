from time import time


def count(fin: int, lim: int) -> int:
    res = 0
    fct = 1
    for i in range(1, fin + 1):
        fct *= i
        if fct <= lim:
            continue
        f = 1
        for j in range(i // 2 + 1):
            if f > lim:
                res += (i + 1) - 2 * j
                break
            f *= i - j
            f //= j + 1
    return res


def count_forum(fin: int, lim: int) -> int:
    res = 0
    binom = [0] * (fin + 1)
    binom[0] = 1
    binom[1] = 1
    for n in range(2, fin + 1):
        for j in range(n, 0, -1):
            binom[j] += binom[j - 1]
            if binom[j] > lim:
                res += j - (n - j) + 1
                break
            j += 1
    return res


t0 = time()
print(count(100, 1_000_000), f"{time() - t0:.3f}")
t0 = time()
print(count_forum(100, 1_000_000), f"{time() - t0:.3f}")
