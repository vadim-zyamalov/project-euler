def sumOnebyOne(nums: list[str]):
    digits = list(zip(*nums))[::-1]
    res = []
    rem = 0

    for dlist in digits:
        dsum = sum(map(int, dlist))
        rem, d = divmod(dsum + rem, 10)
        res.append(d)

    while rem:
        rem, d = divmod(rem, 10)
        res.append(d)

    res.reverse()

    return res


def listToNum(dlist: list[int]) -> int:
    res = 0
    for d in dlist:
        res = 10 * res + d
    return res


with open("p13.txt", "r") as f:
    nums = f.read().strip().split("\n")
    print(listToNum(sumOnebyOne(nums)[:10]))
