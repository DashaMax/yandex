def get_intersection(a: list, b: list) -> list:
    return sorted(list(set(a) & set(b)))


def main():
    list_one = list(map(int, input().split()))
    list_two = list(map(int, input().split()))
    result = get_intersection(list_one, list_two)
    print(*result)


if __name__ == '__main__':
    main()