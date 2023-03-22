def get_min_shots(a: list) -> int:
    shots = set()

    for coord in a:
        shots.add(coord[0])

    return len(shots)


def main():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    result = get_min_shots(coords)
    print(result)


if __name__ == '__main__':
    main()