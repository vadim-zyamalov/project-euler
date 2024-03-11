from utils import primesTo


def solve(limit: int) -> tuple[int, int]:
    primes = primesTo(2 * limit**2 + limit)
    bs = primesTo(1000)
    ba = [(a, 2) for a in range(-998, 1000, 2)] + [
        (a, b) for a in range(-999, 1000, 2) for b in bs[1:]
    ]
    mask = [True] * len(ba)

    n = 0
    while sum(mask) > 1:
        for i, (a, b) in enumerate(ba):
            if not mask[i]:
                continue
            p = n**2 + a * n + b
            if p not in primes:
                mask[i] = False
        n += 1

    return ba[mask.index(True)]


a, b = solve(1000)
print(a * b)
