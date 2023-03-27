def get_frequent_word(a: list) -> str:
    words = {}

    for word in a:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    word = list(words.items())[0]

    for key, value in words.items():
        if value > word[1]:
            word = (key, value)
        elif value == word[1] and key < word[0]:
            word = (key, value)

    return word[0]


def main():
    with open('input.txt') as file:
        text = file.read().split()
    result = get_frequent_word(text)
    print(result)


if __name__ == '__main__':
    main()