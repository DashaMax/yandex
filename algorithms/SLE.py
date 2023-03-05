from random import randint


def is_round(n: float) -> (int, float):
    return round(n, 5) if n * 10 % 10 else int(n)
    # return round(n, 5)


# def sle(*args: str) -> (int, tuple):
#     a, b, c, d, e, f = (int(x) if x.isdigit() else float(x) for x in args)
#     detA = a * d - b * c
#
#     if detA:
#         Aobr = ((d / detA, -b / detA), (-c / detA, a / detA))
#         x = is_round(Aobr[0][0] * e + Aobr[0][1] * f)
#         y = is_round(Aobr[1][0] * e + Aobr[1][1] * f)
#         return 2, x, y
#
#     elif a == b == c == d == e == f == 0:
#         return 5
#
#     elif a == b == 0 != e or c == d == 0 != f:
#         return 0
#
#     elif a * d == b * c != 0 and e * d == f * b != 0:
#         return 1, is_round(-a / b), is_round(e / b)
#
#     elif a == c == 0 and e * d == f * b:
#         if b:
#             return 4, is_round(e / b)
#         return 4, is_round(f / d)
#
#     elif b == d == 0 and e * c == f * a:
#         if a:
#             return 3, is_round(e / a)
#         return 3, is_round(f / c)
#
#     elif (a == b == e == 0 and c and d) or (c == d == f == 0 and a and b):
#         return 5
#
#     return 0


def sle(*args: str) -> (int, tuple):
    a, b, c, d, e, f = (int(x) if x.isdigit() else float(x) for x in args)
    detA = a * d - b * c

    if detA:
        Aobr = ((d / detA, -b / detA), (-c / detA, a / detA))
        x = is_round(Aobr[0][0] * e + Aobr[0][1] * f)
        y = is_round(Aobr[1][0] * e + Aobr[1][1] * f)
        return 2, x, y

    elif a == b == 0:
        if e != 0:
            return 0

        elif c and d:
            return 1, is_round(-c / d), is_round(f / d)

        elif c == d == 0:
            if f != 0:
                return 0
            return 5

        elif c == 0:
            return 4, is_round(f / d)

        elif d == 0:
            return 3, is_round(f / c)

    elif c == d == 0:
        if f != 0:
            return 0

        elif a and b:
            return 1, is_round(-a / b), is_round(e / b)

        elif a == b == 0:
            if e != 0:
                return 0
            return 5

        elif a == 0:
            return 4, is_round(e / b)

        elif b == 0:
            return 3, is_round(e / a)

    elif a == c == 0:
        if b == d == 0:
            if e != 0 or f != 0:
                return 0
            return 5

        elif b == 0:
            if e != 0:
                return 0
            return 4, is_round(f / d)

        elif d == 0:
            if f != 0:
                return 0
            return 4, is_round(e / b)

        elif e * d == b * f:
            return 4, is_round(e / b)

        return 0

    elif b == d == 0:
        if a == c == 0:
            if e != 0 or f != 0:
                return 0
            return 5

        elif a == 0:
            if e != 0:
                return 0
            return 3, is_round(f / c)

        elif c == 0:
            if f != 0:
                return 0
            return 3, is_round(e / a)

        elif e * c == a * f:
            return 3, is_round(e / a)

        return 0

    elif a * d == b * c:
        if e / b == f / d:
            return 1, is_round(-a / b), is_round(e / b)
        return 0


def main():
    a, b, c, d, e, f = (str(randint(0, 1)) for _ in range(6))
    print(a, b, c, d, e, f)
    result = sle(a, b, c, d, e, f)

    if isinstance(result, tuple):
        print(*result)
    else:
        print(result)


def test():
    assert sle(*map(str, (1, 0, 0, 1, 3, 3))) == (2, 3, 3)
    assert sle(*map(str, (3, 6, 7, 2, 3, 7))) == (2, 1, 0)
    assert sle(*map(str, (10, 4, 10, 6, 4, 6))) == (2, 0, 1)

    assert sle(*map(str, (1, 1, 2, 2, 1, 2))) == (1, -1, 1)
    assert sle(*map(str, (2, 1, 2, 1, 1, 1))) == (1, -2, 1)
    assert sle(*map(str, (2, 2, 2, 2, 2, 2))) == (1, -1, 1)
    assert sle(*map(str, (0, 0, 2, 1, 0, 1))) == (1, -2, 1)

    assert sle(*map(str, (0, 2, 0, 4, 1, 2))) == (4, 0.5)
    assert sle(*map(str, (0, 0, 0, 1, 0, 1))) == (4, 1)
    assert sle(*map(str, (0, 2, 0, 0, 0, 0))) == (4, 0)

    assert sle(*map(str, (2, 0, 1, 0, 2, 1))) == (3, 1)
    assert sle(*map(str, (2, 0, 0, 0, 1, 0))) == (3, 0.5)
    assert sle(*map(str, (2, 0, 1, 0, 0, 0))) == (3, 0)
    assert sle(*map(str, (1, 0, 0, 0, 1, 0))) == (3, 1)

    assert sle(*map(str, (0, 0, 9, 10, 9, 5))) == 0
    assert sle(*map(str, (0, 0, 0, 2, 7, 4))) == 0
    assert sle(*map(str, (1, 2, 1, 2, 1, 0))) == 0

    assert sle(*map(str, (0, 0, 0, 0, 0, 0))) == 5


if __name__ == '__main__':
    main()