from random import randint
from time import time


def get_nums(a: list) -> tuple:
    max_1, max_2 = a[0], a[1]
    min_1, min_2 = a[0], a[1]

    for num in a[1:]:
        if num >= max_1:
            max_1, max_2 = num, max_1
        elif num > max_2:
            max_2 = num
        elif num <= min_1:
            min_1, min_2 = num, min_1
        elif num < min_2:
            min_2 = num

    if max_1 * max_2 > min_1 * min_2:
        return max_2, max_1
    return min_1, min_2


def main():
    nums = [randint(-10, 10) for _ in range(10)]
    print(nums)
    time_st = time()
    print(*get_nums(nums))
    print(time() - time_st)


def test():
    assert get_nums([4, 3, 5, 2, 5]) == (5, 5)
    assert get_nums([-4, 3, -5, 2, 5]) == (-5, -4)
    assert get_nums([-4, 0, 0, 2, 0]) == (-4, 0)
    assert get_nums([-4, 3, 8, 4, 9, -2, 0, -4, 3, -3]) == (8, 9)
    assert get_nums([9, -7, 7, 5, -5, -1, -3, 4, -1, -3]) == (7, 9)


if __name__ == '__main__':
    main()