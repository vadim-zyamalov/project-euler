from math import factorial as f


def nthPermutation(n: int) -> int:
    ds = list(range(10))

    res = 0

    while ds:
        lds = len(ds)

        # Если остаток n больше нуля, значит p -- индекс искомой цифры.
        # Если остаток n равен нулю, то перехода к следующей цифре не было
        p, n = divmod(n, f(lds - 1))
        p -= 1 if not n else 0

        res = res * 10 + ds[p]
        ds.remove(ds[p])

    return res


print(nthPermutation(1_000_000))
