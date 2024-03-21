def isPnum(p: int) -> bool:
    n = (1 + (1 + 24 * p) ** 0.5) / 6
    return n.is_integer()


def solve(start: int) -> int:
    h = start + 1
    while True:
        num = h * (2 * h - 1)
        if isPnum(num):
            return num
        h += 1


print(solve(143))
