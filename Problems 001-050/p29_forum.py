from math import sqrt
from math import log
from math import lcm


N = pow(10, 2)


def maxpower(a: int, n: int) -> int:
    return int(log(n) / log(a))


def recurse(step, index, sign, lower_b, upper_b, queue, n):
    if step > upper_b:
        return 0
    res = sign * (upper_b // step - (lower_b - 1) // step)
    for i in range(index + 1, len(queue)):
        res += recurse(
            lcm(step, queue[i]), i, -sign, lower_b, upper_b, queue, n
        )
    return res


def deleteDuplicates(lower_b, upper_b, base_p, cross_p, n, check):
    # Это --- недоступная для меня магия.
    # Не могу понять, почему именно так.
    # Понимаю только, что это число попаданий степеней, кратных cross_b
    # в интервал upper_b--lower_b
    res = upper_b // cross_p - (lower_b - 1) // cross_p

    queue = []
    for i in range(base_p, cross_p):
        if check & (1 << i):
            queue.append(i)

    # Удаляем пересечения с неотфильтрованными степенями с base_p по cross_p
    for i in range(len(queue)):
        res -= recurse(lcm(cross_p, queue[i]), i, 1, lower_b, upper_b, queue, n)

    return res


def countPowers(limit: int) -> list[int]:
    maxP = maxpower(2, limit)

    counts = [0] * (maxP + 1)
    counts[1] = limit - 1

    for base_p in range(2, maxP + 1):
        check = 2 ** (maxP + 1) - 1

        # Это --- недоступная для меня магия.
        # Не могу понять, почему именно так.
        lower_b = (base_p - 1) * limit + 1
        upper_b = base_p * limit

        # Маскируем степени, кратные степеням от base_p до maxP,
        # начиная с 2 * power.
        # Этим исключаем случаи типа 2**4 == 4**2
        # check &= ~(1 << u) <=> check[u] = False
        for i in range(base_p, maxP + 1):
            u = 2 * i
            while u <= maxP:
                check &= ~(1 << u)
                u += i

        # Для каждого неотфильтрованного показателя
        # считаем число итоговых степеней без пересечений с предыдущими
        # неотфильтрованными степенями до base_p
        for cross_p in range(base_p, maxP + 1):
            if check & (1 << cross_p):
                counts[cross_p] += deleteDuplicates(
                    lower_b, upper_b, base_p, cross_p, limit, check
                )

    # Сложный для осознаня кусок
    # Это нужно для того, чтобы для числа, которое можно максимум
    # (без выхода за N) возвести
    # в степень base_p, учесть его меньшие степени.
    for base_p in range(2, maxP + 1):
        counts[base_p] += counts[base_p - 1]

    return counts


counts = countPowers(N)

# Считаем пересечения чисел до корня из N
# Сверх корня встречаются только хвосты последовательностей
rtN = int(sqrt(N))

# Учет степеней уже использованных чисел
used = 0

# Тут будет ответ
res = 0

# Тут учитываются степени сверх корня
# для последующего вычитания
extra_p = 0

for base_num in range(2, rtN + 1):
    if not (used & (1 << base_num)):
        c = maxpower(base_num, N)
        res += counts[c]
        u = base_num
        for counted_p in range(2, c + 1):
            u *= base_num
            if u <= rtN:
                used |= 1 << u
            else:
                extra_p += c - counted_p + 1
                break

# Степени чисел сверх корня
res += (N - rtN) * (N - 1)
res -= extra_p * (N - 1)

print(N, res)
