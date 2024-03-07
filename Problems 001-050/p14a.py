from functools import cache


@cache
def collatz(n: int) -> tuple[int, ...]:
    if n == 1:
        return (1,)

    if n % 2 == 0:
        return (n,) + collatz(n // 2)
    return (n,) + collatz(3 * n + 1)


def solve(limit: int) -> int:
    lmax, imax = 0, -1
    for i in range(1, limit):
        if (nlen := len(collatz(i))) > lmax:
            lmax = nlen
            imax = i
    return imax


print(solve(1_000_000))
