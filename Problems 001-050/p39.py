def countTriangles(p: int) -> int:
    res = 0
    psq = p**2

    for a in range(1, p // 3):
        for b in range(a, (p - a) // 2 + 1):
            if 2 * p * (a + b) + 2 * a * b == psq:
                res += 1

    return res


def countTrianglesOne(p: int) -> int:
    res = 0
    for b in range(1, p // 3):
        a = p * (p - 2 * b) / (2 * (p - b))
        if int(a) == a:
            res += 1
    return res


def solve() -> int:
    res = 0
    ans = 0
    for p in range(3, 1001):
        n = countTrianglesOne(p)
        if res < n:
            res = n
            ans = p

    return ans


print(solve())
