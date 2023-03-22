from random import randint
from time import time


def get_true(a: list, n: int) -> int:
    true = set()

    for i in range(len(a)):
        if a[i][0] >= 0 and a[i][1] >= 0 and sum(a[i]) == n - 1:
            true.add(a[i])

    return len(true)


def main():
    n = int(input())
    phrases = [tuple(map(int, input().split())) for _ in range(n)]
    # n = randint(3, 10)
    # print(n)
    # phrases = [(randint(0, 9), randint(0, 9)) for _ in range(n)]
    # print(phrases)
    # time_start = time()
    result = get_true(phrases, n)
    print(result)
    # print(time() - time_start)


if __name__ == '__main__':
    main()