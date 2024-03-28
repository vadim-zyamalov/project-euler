from time import time
from utils import isPrime, listToNum, numToList, primesTo
from collections import Counter
from itertools import combinations

LIMIT = 1_000_000
primes = primesTo(LIMIT)


def numDbls(num: int) -> list[str]:
    snum = str(num)
    indices = {
        c: [i for i, ch in enumerate(snum) if ch == c and i < len(snum) - 1]
        for c in set(snum)
    }
    res = []
    for idxs in indices.values():
        if len(idxs) > 1:
            for rs in range(2, len(idxs) + 1):
                for cmb in combinations(idxs, r=rs):
                    res.append(
                        "".join("_" if i in cmb else d for i, d in enumerate(snum))
                    )
    return res


def patList(primes: list[int], family: int = 8):
    res = []
    for p in primes:
        res.extend(numDbls(p))
    cnt = Counter(res)

    return [k for k, v in cnt.items() if v == family]


def solve(primes: list[int], family: int = 8) -> int:
    res = LIMIT
    for pat in patList(primes, family):
        for i in range(10):
            num = int(pat.replace("_", str(i)))
            if isPrime(num) and num < res:
                res = num
                break
    return res


t0 = time()
print(solve(primes), f"{time()-t0:.3f}")
