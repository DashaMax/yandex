def is_list_growing(a: list) -> str:
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            return 'NO'
    return 'YES'


def main():
    lst = list(map(float, input().split()))
    print(is_list_growing(lst))


if __name__ == '__main__':
    main()