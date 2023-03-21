from random import choice
from time import time


def get_genom(a: str, b: str) -> int:
    set_genom2 = set()
    count = 0

    for i in range(len(b) - 1):
        set_genom2.add(b[i:i + 2])

    for i in range(len(a) - 1):
        if a[i:i + 2] in set_genom2:
            count += 1

    return count


def main():
    genom_one = input()
    genom_two = input()
    # genom_one = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(100000))
    # genom_two = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(100000))
    # print(genom_one)
    # print(genom_two)
    # time_start = time()
    result = get_genom(genom_one, genom_two)
    print(result)
    # print(time() - time_start)


if __name__ == '__main__':
    main()