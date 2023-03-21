def get_buts(c: list, a: list) -> int:
    setCalc = set(c)
    setNum = set(a)
    return len(setNum - setCalc)


def main():
    calc = list(map(int, input().split()))
    n = [int(x) for x in input()]
    result = get_buts(calc, n)
    print(result)


if __name__ == '__main__':
    main()