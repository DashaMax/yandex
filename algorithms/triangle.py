def check_triangle(a: int, b: int, c: int) -> str:
    if a < b + c and b < a + c and c < a + b:
        return 'YES'
    return 'NO'


def main():
    a, b, c = int(input()), int(input()), int(input())
    is_triangle = check_triangle(a, b, c)
    print(is_triangle)


def test():
    assert check_triangle(1, 2, 3) == 'NO'
    assert check_triangle(4, 3, 5) == 'YES'
    assert check_triangle(1, 1, 1) == 'YES'
    assert check_triangle(4, 4, 9) == 'NO'


if __name__ == '__main__':
    main()