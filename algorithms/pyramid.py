def get_max_height(a: list) -> int:
    blocks = {}

    for block in a:
        if block[0] not in blocks or block[1] > blocks[block[0]]:
            blocks[block[0]] = block[1]

    return sum(blocks.values())


def main():
    n = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(n)]
    result = get_max_height(blocks)
    print(result)


if __name__ == '__main__':
    main()