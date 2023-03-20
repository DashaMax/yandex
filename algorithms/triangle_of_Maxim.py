from random import randint, choice
from time import time


def get_frequency_of_triangle(a: list) -> tuple:
    min_frequency, max_frequency = 30.0, 4000.0
    previous = a[0][0]

    for i in range(1, len(a)):
        middle = round((a[i][0] + a[i - 1][0]) / 2, 6)

        if a[i][1] == 'closer' and a[i][0] >= previous or a[i][1] == 'further' and a[i][0] <= previous:
            min_frequency = max(min_frequency, middle)
        else:
            max_frequency = min(max_frequency, middle)

        previous = a[i][0]

    return min_frequency, max_frequency


def main():
    n = int(input())
    frequencies = [(float(input()), '')]

    # n = randint(2, 1000)
    # frequencies = [(float(randint(30, 4000)), '')]

    for _ in range(n - 1):
        s = input().split()
        frequencies.append((float(s[0]), s[1]))

    # for _ in range(n - 1):
    #     frequencies.append((float(randint(30, 4000)), choice(('closer', 'further'))))

    # print(frequencies)
    # time_start = time()

    result = get_frequency_of_triangle(frequencies)
    print(*result)

    # print(time() - time_start)


if __name__ == '__main__':
    main()