def neighbors(a: list) -> int:
    count = 0

    for i in range(1, len(a) - 1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            count += 1

    return count


def main():
    nums = list(map(int, input().split()))
    print(neighbors(nums))


if __name__ == '__main__':
    main()