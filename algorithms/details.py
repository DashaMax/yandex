from time import time
from random import randint


def get_details(n: int, k: int, m: int) -> int:
    details = 0

    if n < k or k < m:
        return details

    while n >= k:
        details += k // m
        n -= (k // m) * m

    return details


def main():
    n, k, m = (randint(1, 200) for _ in range(3))
    print(n, k, m)
    print(get_details(n, k, m))


def test():
    assert get_details(10, 5, 2) == 4
    assert get_details(13, 5, 3) == 3
    assert get_details(14, 5, 3) == 4
    assert get_details(107, 101, 14) == 7
    assert get_details(153, 75, 13) == 10
    assert get_details(54, 77, 85) == 0
    assert get_details(179, 77, 85) == 0


if __name__ == '__main__':
    time_st = time()
    main()
    print(time() - time_st)