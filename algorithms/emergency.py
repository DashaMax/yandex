from math import ceil, floor
from random import randint
from time import time


def emergency(*args) -> tuple:
    k1, m, k2, p2, n2 = args

    if n2 > m or k2 < m * (p2 - 1) + n2:
        return -1, -1

    elif k1 == 1:
        return 1, 1

    elif p2 == n2 == 1:
        if k1 <= k2:
            return 1, 1
        elif m == 1:
            return 0, 1
        elif k1 <= m * k2:
            return 1, 0
        return 0, 0

    n_flat_left = k2 / (n2 + m * (p2 - 1))
    n_flat_right = k2 / (n2 - 1 + m * (p2 - 1))
    n_flat = [x for x in range(floor(n_flat_left), ceil(n_flat_right)) if n_flat_left <= x < n_flat_right]

    if not n_flat:
        return -1, -1

    p1 = [ceil(k1 / (m * x)) for x in n_flat]
    n1 = [ceil((k1 - (p1[i] - 1) * m * n_flat[i]) / n_flat[i]) for i in range(len(n_flat))]

    if len(set(p1)) == len(set(n1)) == 1:
        return p1[0], n1[0]
    elif len(set(p1)) == 1:
        return p1[0], 0
    elif len(set(n1)) == 1:
        return 0, n1[0]
    return 0, 0


def main():
    k1, m, k2, p2, n2 = [randint(1, 20) for _ in range(5)]
    print(k1, m, k2, p2, n2)
    print(*emergency(k1, m, k2, p2, n2))


def test():
    assert emergency(11, 20, 167, 3, 2) == (1, 3)
    assert emergency(89, 20, 41, 1, 11) == (2, 3)
    assert emergency(11, 1, 1, 1, 1) == (0, 1)
    assert emergency(11, 12, 10, 1, 4) == (1, 4)
    assert emergency(12, 12, 10, 1, 1) == (1, 0)
    assert emergency(1, 1, 3, 1, 1) == (1, 1)
    assert emergency(1, 6, 10, 1, 1) == (1, 1)
    assert emergency(2, 5, 1, 1, 1) == (1, 0)
    assert emergency(3, 2, 2, 2, 1) == (-1, -1)
    assert emergency(16, 2, 1, 3, 1) == (-1, -1)
    assert emergency(7, 1, 10, 5, 6) == (-1, -1)
    assert emergency(1, 9, 3, 1, 11) == (-1, -1)
    assert emergency(1, 9, 3, 1, 7) == (-1, -1)


if __name__ == '__main__':
    time_st = time()
    main()
    print(time() - time_st)