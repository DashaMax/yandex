from time import time
from random import randint


def get_size_table(*args) -> tuple:
    a1, b1, a2, b2 = args
    squares = []
    laptop_sizes = [(max(a1, b1), min(a1, b1)), (max(a2, b2), min(a2, b2))]
    laptop_sizes.sort(key=lambda x: x[0], reverse=True)

    length_1, width_1 = laptop_sizes[0][0] + laptop_sizes[1][0], max((laptop_sizes[0][1], laptop_sizes[1][1]))
    length_2, width_2 = laptop_sizes[0][0], laptop_sizes[0][1] + laptop_sizes[1][1]
    length_3, width_3 = laptop_sizes[0][0] + laptop_sizes[1][1], max((laptop_sizes[0][1], laptop_sizes[1][0]))

    squares.append(length_1 * width_1)
    squares.append(length_2 * width_2)
    squares.append(length_3 * width_3)
    min_square = min(squares)

    if squares[0] == min_square:
        return length_1, width_1
    elif squares[1] == min_square:
        return length_2, width_2
    return length_3, width_3


def main():
    a1, b1, a2, b2 = (randint(1, 1000) for _ in range(4))
    print(a1, b1, a2, b2)
    print(*get_size_table(a1, b1, a2, b2))


def test():
    assert get_size_table(10, 2, 2, 10) == (20, 2) or (2, 20) or (4, 10) or (10, 4)
    assert get_size_table(5, 7, 3, 2) == (9, 5) or (5, 9)


if __name__ == '__main__':
    time_st = time()
    main()
    print(time() - time_st)