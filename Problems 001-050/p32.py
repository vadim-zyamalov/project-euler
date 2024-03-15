from itertools import permutations as perms
from functools import cache


POSS = [(1, 5), (2, 5)]


@cache
def num(digits: tuple[int, ...]) -> int:
    res = 0
    for d in digits:
        res = 10 * res + d
    return res


def solve() -> int:
    nums = set()
    for digits in perms(range(1, 10)):
        for p0, p1 in POSS:
            if num(digits[:p0]) * num(digits[p0:p1]) == num(digits[p1:]):
                nums.add(num(digits[p1:]))

    return sum(nums)


print(solve())
