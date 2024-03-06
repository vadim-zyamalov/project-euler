def solve(n: int) -> int:
    ns = [(i, n // i) for i in [3, 5, 15]]
    sums = [i * (nn + 1) * nn // 2 for i, nn in ns]
    return sums[0] + sums[1] - sums[2]


print(solve(999))
