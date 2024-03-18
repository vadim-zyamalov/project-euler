from time import time


def solve(limit: int) -> int:
    res = 0
    for i in range(1, limit, 2):
        n = f"{i}"
        nb = f"{i:b}"
        if n == n[::-1] and nb == nb[::-1]:
            res += i
    return res


def genPalyndrome(num: int, odd=False) -> int:
    res = num
    if odd:
        num //= 10
    while num:
        num, d = divmod(num, 10)
        res = res * 10 + d
    return res


def genPalyndrome2(num: int, odd=False) -> int:
    res = num
    if odd:
        num >>= 1
    while num:
        res = (res << 1) + (num & 1)
        num >>= 1
    return res


def isPalyndrome(num: int, base: int = 10) -> bool:
    rev = 0
    _num = num

    while _num:
        _num, d = divmod(_num, base)
        rev = rev * base + d

    return rev == num


def solve_forum(limit: int) -> int:
    res = 0
    i = 1
    while True:
        np = genPalyndrome(i)
        if np > limit:
            break
        res += 1 if isPalyndrome(np, 2) else 0
        print(f"{np} : {np:b} : {isPalyndrome(np, 2)}")
        i += 1
    i = 1
    while True:
        np = genPalyndrome(i, True)
        if np > limit:
            break
        res += 1 if isPalyndrome(np, 2) else 0
        print(f"{np} : {np:b} : {isPalyndrome(np, 2)}")
        i += 1
    return res


t0 = time()
print(solve(1_000_000), f"{time() - t0:.3f}")
t0 = time()
print(solve_forum(1_000_000), f"{time() - t0:.3f}")
