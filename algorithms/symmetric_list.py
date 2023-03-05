from random import randint


def add_num(a: list) -> (int, tuple):
    a_reverse = a[::-1]
    index = None
    i = j = 0

    while i < len(a):
        i += 1
        if a[i - 1] != a_reverse[j]:
            index = i - 1
            j = 0
            continue
        j += 1

    if index is None:
        return 0

    add_nums = a[index::-1]
    return len(add_nums), add_nums


def main():
    lst = [randint(1, 9) for _ in range(100)]
    result = add_num(lst)

    if isinstance(result, int):
        print(result)
    else:
        print(result[0], ' '.join(map(str, *result[1:])), sep='\n')


if __name__ == '__main__':
    main()