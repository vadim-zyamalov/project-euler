from time import time
from itertools import permutations


CHECKS = {
    17: (1000, 1),
    13: (10000, 10),
    11: (100000, 100),
    7: (1000000, 1000),
    5: (10000000, 10000),
    3: (100000000, 100000),
    2: (1000000000, 1000000),
}


def checkNum(num: tuple[int, ...]) -> int:
    n = 0
    for d in num:
        n = 10 * n + d
    if all(((n % d0) // d1) % p == 0 for p, (d0, d1) in CHECKS.items()):
        return n
    return 0


def solve():
    return sum(checkNum(num) for num in permutations(range(10)) if num[0] != 0)


def construct(divs=[17, 13, 11, 7, 5, 3, 2], nums=[]):
    if not divs:
        return [
            int(c + num) for c in "0123456789" for num in nums if c not in num
        ]

    p = divs.pop(0)
    cur = []

    for n in range(p, 1000, p):
        nstr = str(n).zfill(3)
        if p == 17 and len(set(nstr)) == len(nstr):
            cur.append(nstr)
        else:
            for tail in nums:
                if nstr[1:] == tail[:2] and len(set(nstr[0] + tail)) == len(
                    nstr[0] + tail
                ):
                    cur.append(nstr[0] + tail)

    return construct(divs, cur)


t0 = time()
print(solve(), f"{time()-t0:.3f}")
t0 = time()
print(sum(construct()), f"{time()-t0:.3f}")
