def get_nums(a: list) -> str:
    words = {}
    result = ''

    for word in a:
        if word not in words:
            words[word] = 0
            result += '0 '
        else:
            words[word] += 1
            result += str(words[word]) + ' '

    return result


def main():
    with open('input.txt') as file:
        words = file.read().split()
    result = get_nums(words)
    print(result)


if __name__ == '__main__':
    main()