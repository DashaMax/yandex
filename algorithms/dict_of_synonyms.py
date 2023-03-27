def get_synonym(d: dict, word: str) -> str:
    for key, value in d.items():
        if word == value:
            return key
        elif word == key:
            return value


def main():
    n = int(input())
    dict_synonyms = {}

    for _ in range(n):
        pair = input().split()
        dict_synonyms[pair[0]] = pair[1]

    word = input()
    result = get_synonym(dict_synonyms, word)
    print(result)


if __name__ == '__main__':
    main()