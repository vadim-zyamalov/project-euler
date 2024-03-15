from time import time
from math import log10
from utils import primesTo
from itertools import product


def rotate(num):
    n = int(log10(num))
    h, t = divmod(num, 10)
    return t * 10**n + h


def num(digits: tuple[int, ...]) -> int:
    res = 0
    for d in digits:
        res = res * 10 + d
    return res


def solve(limit: int) -> int:
    primes = primesTo(limit)
    checked = []

    for p in primes:
        if p in checked:
            continue
        stop = False
        rotates = [p]
        _p = p
        for _ in range(int(log10(p))):
            _p = rotate(_p)
            if _p % 10 == 0:
                stop = True
                break
            if _p in primes:
                rotates.append(_p)
            else:
                stop = True
                break
        if stop:
            continue
        checked.extend(set(rotates))

    return len(checked)


def solve_forum(limit: int) -> int:
    digits = [1, 3, 7, 9]
    primes = primesTo(limit)

    checked = [2, 5]

    for N in range(1, 7):
        for ds in product(digits, repeat=N):
            p = num(ds)
            if p in checked:
                continue
            tmp = [p]
            for _ in range(N - 1):
                ds = ds[-1:] + ds[:-1]
                tmp.append(num(ds))
            if all(n in primes for n in tmp):
                checked.extend(set(tmp))

    return len(checked)


t0 = time()
print(solve(1_000_000), f"{time()-t0:.2f}")
t0 = time()
print(solve_forum(1_000_000), f"{time()-t0:.2f}")
