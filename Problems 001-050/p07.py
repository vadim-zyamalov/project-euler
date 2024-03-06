from utils import primeLim, primesTo


def solve(n: int) -> int:
    limit = primeLim(n)
    return primesTo(limit)[n - 1]


print(solve(10_001))
