from math import log10
from utils import numToList


def digitsNum(num):
    return int(log10(num) + 1)


def solve(nums):
    res = sum(nums)
    return res // 10 ** (digitsNum(res) - 10)


with open("0013_numbers.txt", "r") as f:
    nums = list(map(int, f.read().strip().split("\n")))
    print(solve(nums))
