from random import randint
from time import time


def get_operations(a: list) -> int:
    operation = 0

    if len(set(a)) == 1:
        return operation

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return -1

        if a[i] < a[i + 1]:
            operation += a[i + 1] - a[i]

    return operation


def main():
    n = int(input())
    volumes = list(map(int, input().split()))
    # volumes = [randint(1, 10000000) for _ in range(100000)]
    # volumes.sort()
    # print(volumes)
    # time_start = time()
    result = get_operations(volumes)
    print(result)
    # print(time() - time_start)


def test():
    assert get_operations([1, 2]) == 1
    assert get_operations([1, 1, 5, 5, 5]) == 4
    assert get_operations([3, 2, 1]) == -1


if __name__ == '__main__':
    main()