ONES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def spellNum(num: int) -> str:
    res = ""

    num, q = divmod(num, 100)
    if q == 0:
        pass
    elif q < 20:
        res = f" {ONES[q]}" + res
    else:
        d0, d1 = divmod(q, 10)
        if d1:
            res = f" {TENS[d0]}-{ONES[d1]}" + res
        else:
            res = f" {TENS[d0]}" + res

    if num:
        if res:
            res = " and" + res
        d0, d1 = divmod(num, 10)
        if d1:
            res = f" {ONES[d1]} hundred" + res
        if d0:
            res = f"{ONES[d0]} thousand" + res

    return res.strip()


def lenNum(snum: str) -> int:
    return sum(el not in ["-", " "] for el in snum)


print(sum(lenNum(spellNum(i)) for i in range(1, 1001)))
