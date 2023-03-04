from random import randint


def is_throw_away(*args: int) -> str:
    a, b, c, d, e = args

    if max((a, b)) <= max((d, e)) and min((a, b)) <= min((d, e)) or \
       max((a, c)) <= max((d, e)) and min((a, c)) <= min((d, e)) or \
       max((b, c)) <= max((d, e)) and min((b, c)) <= min((d, e)):
        return 'YES'
    return 'NO'


def main():
    a, b, c, d, e = (randint(1, 10) for _ in range(5))
    print(a, b, c, d, e)
    print(is_throw_away(a, b, c, d, e))


def test():
    assert is_throw_away(1, 1, 1, 1, 1) == 'YES'
    assert is_throw_away(2, 2, 2, 1, 1) == 'NO'
    assert is_throw_away(7, 5, 5, 4, 10) == 'NO'


if __name__ == '__main__':
    main()