from math import log


def primesTo(num):
    result = [2]

    if num == 2:
        return result

    marked = [False] * (num // 2)

    for p in range(3, num + 1, 2):
        if marked[(p - 3) // 2]:
            continue
        result += [p]
        for mul in range(p**2, num, 2 * p):
            marked[(mul - 3) // 2] = True

    return result


def primeLim(n: int) -> int:
    return int(n * log(n) + n * log(log(n)))


def gcd(x: int, y: int) -> int:
    if abs(x) < abs(y):
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


def gcdL(xs: list[int]) -> int:
    x = xs[0]

    for y in xs[1:]:
        x = gcd(x, y)

    return x


def lcm(x: int, y: int) -> int:
    return abs(x * y) // gcd(x, y)


def lcmL(xs: list[int]) -> int:
    x = xs[0]

    for y in xs[1:]:
        x = lcm(x, y)

    return x
