def get_languages(a: list) -> tuple:
    all_ = set(a[0])
    one_ = set(a[0])

    for i in range(1, len(a)):
        all_ &= set(a[i])
        one_ |= set(a[i])

    return all_, one_


def main():
    n = int(input())
    languages = []

    for i in range(n):
        m = int(input())
        language_i = []

        for j in range(m):
            language_i.append(input())

        languages.append(tuple(language_i))

    result = get_languages(languages)

    for res in result:
        print(len(res))

        for language in res:
            print(language)


if __name__ == '__main__':
    main()