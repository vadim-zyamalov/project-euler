def sumEvenFibs(limit: int) -> int:
    if limit < 2:
        return 0
    if limit < 8:
        return 2

    res = 2
    f0, f1 = 2, 8

    while True:
        if f1 >= limit:
            break
        res += f1
        f0, f1 = f1, 4 * f1 + f0

    return res


print(sumEvenFibs(4_000_000))
