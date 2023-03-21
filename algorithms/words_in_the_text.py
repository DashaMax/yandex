import sys


def get_words(a: list) -> int:
    return len(set(a))


def main():
    text = sys.stdin.read().split()
    result = get_words(text)
    print(result)


if __name__ == '__main__':
    main()