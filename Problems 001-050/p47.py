from utils import factor


def search():
    i = 2 * 3 * 5 * 7
    c = 0

    while c != 4:
        fcur = factor(i)
        if len(fcur.keys()) == 4:
            c += 1
        else:
            c = 0
        i += 1

    return i - 4


print(search())
