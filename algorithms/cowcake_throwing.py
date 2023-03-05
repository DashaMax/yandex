from random import randint
from time import time


def rank_vasilij(a: list) -> int:
    max_player = 0
    index_winner = a.index(max(a))

    for i in range(1, len(a) - 1):
        if a[i] % 5 == 0 and a[i] % 10 != 0 and \
           a[i + 1] < a[i] and index_winner < i and a[i] > max_player:
            max_player = a[i]

    if not max_player:
        return 0

    a.sort(reverse=True)
    return a.index(max_player) + 1


def main():
    distance = [randint(1, 1000) for _ in range(randint(3, 10 ** 5))]
    print(distance)
    time_st = time()
    print(rank_vasilij(distance))
    print(time() - time_st)


if __name__ == '__main__':
    main()