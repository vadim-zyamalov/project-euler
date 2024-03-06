def isPalyndrome(num: int) -> bool:
    snum = str(num)
    return snum == snum[::-1]


def isPalyndromeN(num: int) -> bool:
    rev = 0
    orig = num

    while num:
        rev = rev * 10 + num % 10
        num //= 10

    return orig == rev


def pair(lb: int, ub: int):
    res = 0
    for i in range(lb, ub):
        for j in range(i, ub):
            if isPalyndrome(tmp := i * j):
                res = max(res, tmp)
    return res


print(pair(100, 1000))
