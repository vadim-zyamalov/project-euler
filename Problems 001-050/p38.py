from math import log10


def concatProd(num: int) -> int:
    res = 0
    l = 0
    n = 1
    while True:
        tmp = num * n
        ltmp = int(log10(tmp)) + 1
        res = res * 10**ltmp + tmp
        l += ltmp
        if l == 9:
            break
        if l > 9:
            return -1
        n += 1
    count = {}
    _res = res
    while _res:
        _res, d = divmod(_res, 10)
        count[d] = count.get(d, 0) + 1
    if sorted(count.keys()) == list(range(1, 10)):
        return res
    return -1


def concatProdStr(num: int) -> int:
    res = ""
    n = 1
    while True:
        res += str(num * n)
        n += 1
        if len(res) == 9:
            if sorted(res) == list("123456789"):
                return int(res)
        if len(res) > 9:
            return -1


def solve():
    res = 0
    for n in range(1, 9876):
        num = concatProd(n)
        res = max(res, num)
    return res


print(solve())
