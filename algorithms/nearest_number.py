def nearest_number(a: list, n: int) -> int:
    diff = abs(n - a[0])
    num = a[0]

    for i in range(1, len(a)):
        if abs(n - a[i]) <= diff:
            diff = abs(n - a[i])
            num = a[i]

    return num


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    x = int(input())
    print(nearest_number(numbers, x))


if __name__ == '__main__':
    main()