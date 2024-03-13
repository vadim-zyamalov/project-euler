from math import log, sqrt, lcm


def powerOverlaps(limit: int) -> dict[int, int]:
    powers = {}
    maxPower = int(log(limit) / log(2))

    for p in range(2, maxPower + 1):
        mask = 0
        for k in range(1, p):
            step = lcm(p, k) // p

            n = 0
            while n <= k * limit / p:
                mask |= 1 << n
                n += step
        for j in range(2, limit + 1):
            if mask & (1 << j):
                powers[p] = powers.get(p, 0) + 1

    return powers


def realPowers(limit: int) -> dict[int, int]:
    powers = {}
    maxNum = int(sqrt(limit))
    prohibited = 0

    for n in range(2, maxNum + 1):
        if prohibited & (1 << n):
            continue

        p = 2
        while n**p <= limit:
            powers[p] = powers.get(p, 0) + 1
            if n**p <= maxNum:
                prohibited |= 1 << n**p
            p += 1

    return powers


def solve(limit: int) -> int:
    doubles = 0
    overlaps = powerOverlaps(limit)
    reals = realPowers(limit)
    for k in reals:
        doubles += reals[k] * overlaps[k]

    return (limit - 1) * (limit - 1) - doubles


print(solve(pow(10, 3)))
