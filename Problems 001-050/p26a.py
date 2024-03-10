# 1. Brent R.P. An improved Monte Carlo factorization algorithm /
# R.P. Brent //
# BIT Numerical Mathematics. – 1980. – Vol. 20. – № 2. – P. 176-184.


from typing import Callable


def brentCycle(f: Callable, x0: int) -> tuple[int, int]:
    pwr = lbd = 1
    p0 = x0
    p1 = f(x0)

    while p0 != p1:
        if pwr == lbd:
            p0 = p1
            pwr *= 2
            lbd = 0
        p1 = f(p1)
        lbd += 1

    p0 = p1 = x0
    for _ in range(lbd):
        p1 = f(p1)

    mu = 0
    while p0 != p1:
        p0, p1 = f(p0), f(p1)
        mu += 1

    return mu, lbd


def lambdaGen(d: int) -> Callable:
    return lambda x: (10 * x) % d


maxl = 0
maxd = 0
for d in range(2, 1000):
    _, l = brentCycle(lambdaGen(d), 1)
    if l > maxl:
        maxl = l
        maxd = d
print(maxd)
