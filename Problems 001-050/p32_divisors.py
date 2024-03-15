# luke_earthwalker

from math import sqrt


def divs(n: int) -> list[tuple[int, int]]:
    return [(i, n // i) for i in range(1, int(sqrt(n)) + 1) if n % i == 0]


def solve() -> int:
    nums = set()
    for i in range(1, 10000):
        for d0, d1 in divs(i):
            if sorted(f"{d0}{d1}{d0*d1}") == list("123456789"):
                nums.add(d0 * d1)
    return sum(nums)


print(solve())
