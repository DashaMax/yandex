from random import randint


def get_time(arg1: int, arg2: int) -> tuple:
    t_min = (arg2 - 1) * (arg1 + 1) + 1
    t_max = arg2 * (arg1 + 1) + arg1
    return t_min, t_max


def subway(*args) -> (int, tuple):
    way_1 = get_time(args[0], args[2])
    way_2 = get_time(args[1], args[3])

    if max((way_1[0], way_2[0])) <= min((way_1[1], way_2[1])):
        return max((way_1[0], way_2[0])), min((way_1[1], way_2[1]))
    return -1


def main():
    a, b, n, m = (randint(1, 10) for _ in range(4))
    print(a, b, n, m)
    result = subway(a, b, n, m)

    if isinstance(result, tuple):
        print(*result)
    else:
        print(result)


def test():
    assert subway(1, 3, 3, 2) == (5, 7)
    assert subway(1, 7, 9, 2) == (17, 19)
    assert subway(1, 2, 2, 1) == (3, 5)
    assert subway(1, 5, 1, 2) == -1
    assert subway(4, 1, 5, 3) == -1


if __name__ == '__main__':
    main()