def modpower(num, p, m):
    if p == 0:
        return 1
    res = modpower(num, p // 2, m)
    if p & 1:
        return (num * res * res) % m
    return (res * res) % m


def solve(limit: int) -> int:
    res = 0
    for i in range(1, limit + 1):
        res += modpower(i, i, 10**10)
        res %= 10**10
    return res


print(solve(1_000))
