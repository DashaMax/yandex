from random import randint


def equation_with_root(a: int, b: int, c: int) -> (str, int):
    if c < 0 or a == 0 and c ** 2 != b:
        return 'NO SOLUTION'

    elif a == b == c == 0 or a == 0 and c ** 2 == b:
        return 'MANY SOLUTIONS'

    x = (c ** 2 - b) / a

    if a * x + b < 0 or int(x) != x:
        return 'NO SOLUTION'
    return int(x)


def main():
    a, b, c = randint(-5, 5), randint(-5, 5), randint(-2, 5)
    print(a, b, c)
    print(equation_with_root(a, b, c))


def test():
    assert equation_with_root(1, 0, 0) == 0
    assert equation_with_root(1, 2, 3) == 7
    assert equation_with_root(-4, 5, 1) == 1
    assert equation_with_root(-1, -2, 3) == -11

    assert equation_with_root(0, 0, 0) == 'MANY SOLUTIONS'
    assert equation_with_root(0, 16, 4) == 'MANY SOLUTIONS'

    assert equation_with_root(0, 16, -4) == 'NO SOLUTION'
    assert equation_with_root(0, 16, 2) == 'NO SOLUTION'
    assert equation_with_root(1, 2, -3) == 'NO SOLUTION'
    assert equation_with_root(3, 6, 4) == 'NO SOLUTION'
    assert equation_with_root(0, -36, 6) == 'NO SOLUTION'


if __name__ == '__main__':
    main()