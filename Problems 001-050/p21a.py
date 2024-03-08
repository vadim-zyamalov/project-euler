from math import ceil, sqrt


def divisors(num: int) -> list[int]:
    res = [1]
    if num < 4:
        return res
    for i in range(2, ceil(sqrt(num))):
        j, q = divmod(num, i)
        if q == 0:
            res.append(i)
            if i != j:
                res.append(j)

    return sorted(res)


def amicable(limit: int) -> list[int]:
    num_sum = {}
    res = []

    for i in range(2, limit):
        s = sum(divisors(i))
        num_sum[i] = s

    for i, s in num_sum.items():
        if i >= s:
            continue
        if s in num_sum and num_sum[s] == i:
            res.append((i, s))
    return res


res = set(el for p in amicable(10000) for el in p)
print(sum(res))
