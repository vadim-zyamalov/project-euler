def yearCal(year: int) -> list[int]:
    leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    return (
        list(range(1, 31 + 1))  # Jan
        + list(range(1, 29 + 1 if leap else 28 + 1))  # Feb
        + list(range(1, 31 + 1))  # Mar
        + list(range(1, 30 + 1))  # Apr
        + list(range(1, 31 + 1))  # May
        + list(range(1, 30 + 1))  # Jun
        + list(range(1, 31 + 1))  # Jul
        + list(range(1, 31 + 1))  # Aug
        + list(range(1, 30 + 1))  # Sep
        + list(range(1, 31 + 1))  # Oct
        + list(range(1, 30 + 1))  # Nov
        + list(range(1, 31 + 1))  # Dec
    )


def countSundays(beg: int, fin: int) -> int:
    extra = len(yearCal(1900)) % 7
    res = 0

    for y in range(beg, fin + 1):
        cal = [0] * extra + yearCal(y)
        extra = len(cal) % 7
        res += len([d for i, d in enumerate(cal) if d == 1 and i % 7 == 6])

    return res


print(countSundays(1901, 2000))
