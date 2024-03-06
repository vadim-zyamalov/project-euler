def solve(num: int) -> list[int]:
    res = []
    for a in range(1, num // 3):
        for b in range(a, (num - a) // 2 + 1):
            c = num - a - b
            if a**2 + b**2 == c**2:
                res += [a * b * c]
    return res


print(solve(1000))
