def get_count_different_numbers(a: list) -> int:
    return len(set(a))


def main():
    numbers = list(map(int, input().split()))
    result = get_count_different_numbers(numbers)
    print(result)


if __name__ == '__main__':
    main()