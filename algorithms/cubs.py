def get_cubs(a: list, b: list) -> tuple:
    setA = set(a)
    setB = set(b)
    colors = sorted(tuple(setA & setB))
    cubsA = sorted(tuple(setA - setB))
    cubsB = sorted(tuple(setB - setA))
    return colors, cubsA, cubsB


def main():
    n, m = map(int, input().split())
    cubsA = [int(input()) for _ in range(n)]
    cubsB = [int(input()) for _ in range(m)]
    result = get_cubs(cubsA, cubsB)

    for x in result:
        print(len(x))
        print(*x)


if __name__ == '__main__':
    main()