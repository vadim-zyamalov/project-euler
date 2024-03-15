from utils import fact


F = [fact(i) for i in range(10)]


def solve() -> int:
    res = 0

    for i in range(10, F[9] * 7):
        _i = i
        tmp = 0
        stop = False
        while _i:
            _i, d = divmod(_i, 10)
            tmp += F[d]

        if tmp == i:
            res += i

    return res


print(solve())
