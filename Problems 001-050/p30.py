def checkSum(num: int) -> bool:
    test = 0
    _num = num

    while _num:
        test += (_num % 10) ** 5
        _num //= 10

    return num == test


LIMIT = 6 * 9**5

res = 0
for num in range(2, LIMIT):
    if checkSum(num):
        res += num

print(res)
