from random import randint
from time import time


def get_nums(a: list) -> tuple:
    if a[0] >= a[1] and a[0] >= a[2]:
        max_1 = a[0]

        if a[1] >= a[2]:
            max_2, max_3 = a[1], a[2]
        else:
            max_2, max_3 = a[2], a[1]

    elif a[1] >= a[0] and a[1] >= a[2]:
        max_1 = a[1]

        if a[0] >= a[2]:
            max_2, max_3 = a[0], a[2]
        else:
            max_2, max_3 = a[2], a[0]

    elif a[2] >= a[1] and a[2] >= a[0]:
        max_1 = a[2]

        if a[1] >= a[0]:
            max_2, max_3 = a[1], a[0]
        else:
            max_2, max_3 = a[0], a[1]

    min_1, min_2 = max_3, max_2

    for i in range(3, len(a)):
        if a[i] >= max_1:
            max_1, max_2, max_3 = a[i], max_1, max_2
        elif a[i] >= max_2:
            max_2, max_3 = a[i], max_2
        elif a[i] > max_3:
            max_3 = a[i]
        elif a[i] < min_1:
            min_1, min_2 = a[i], min_1
        elif a[i] < min_2:
            min_2 = a[i]

    if max_1 * max_2 * max_3 >= max_1 * min_1 * min_2:
        return max_1, max_2, max_3
    elif max_1 * min_1 * min_2 >= max_1 * max_2 * max_3:
        return max_1, min_1, min_2


def main():
    lst = list(map(int, input().split()))
    # lst = [randint(-100, 100) for _ in range(randint(3, 50))]
    # print(lst)
    # time_start = time()
    result = get_nums(lst)
    print(*result)
    # print(time() - time_start)


def test():
    assert get_nums([3, 5, 1, 7, 9, 0, 9, -3, 10]) == (10, 9, 9)
    assert get_nums([-5, -3000, -12]) == (-5, -12, -3000)
    assert get_nums([1, 2, 3]) == (3, 2, 1)
    assert get_nums([-18, -61, 89]) == (89, -18, -61)


if __name__ == '__main__':
    main()