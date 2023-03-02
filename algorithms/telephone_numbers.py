from time import time


def check_number(num: str, n: str) -> str:
    n = ''.join(x for x in n if x.isdigit())
    num = ''.join(x for x in num if x.isdigit())
    n = n[1:] if len(n) == 11 else '495' + n
    num = num[1:] if len(num) == 11 else '495' + num

    if num == n:
        return 'YES'
    return 'NO'


def main():
    number_add = input()
    numbers = [input() for _ in range(3)]

    time_st = time()

    for num in numbers:
        print(check_number(num, number_add))

    print(time() - time_st)


def test():
    assert check_number('8(495)430-23-97', '+7-4-9-5-43-023-97') == 'YES'
    assert check_number('8(495)430-23-97', '4-3-0-2-3-9-7') == 'YES'
    assert check_number('8(495)430-23-97', '8-495-430') == 'NO'

    assert check_number('86406361642', '83341994118') == 'NO'
    assert check_number('86406361642', '86406361642') == 'YES'
    assert check_number('86406361642', '83341994118') == 'NO'

    assert check_number('+78047952807', '+78047952807') == 'YES'
    assert check_number('+78047952807', '+76147514928') == 'NO'
    assert check_number('+78047952807', '88047952807') == 'YES'


if __name__ == '__main__':
    main()