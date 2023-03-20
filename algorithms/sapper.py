def get_field_sapper(rws: int, cls: int, coords: list) -> list:
    field = [['*' if (i + 1, j + 1) in coords else 0 for j in range(cls)] for i in range(rws)]

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] != '*':
                if i - 1 >= 0 and j - 1 >= 0 and field[i - 1][j - 1] == '*':
                    field[i][j] += 1
                if i - 1 >= 0 and field[i - 1][j] == '*':
                    field[i][j] += 1
                if i - 1 >= 0 and j + 1 < len(field[i]) and field[i - 1][j + 1] == '*':
                    field[i][j] += 1
                if j - 1 >= 0 and field[i][j - 1] == '*':
                    field[i][j] += 1
                if j + 1 < len(field[i]) and field[i][j + 1] == '*':
                    field[i][j] += 1
                if i + 1 < len(field) and j - 1 >= 0 and field[i + 1][j - 1] == '*':
                    field[i][j] += 1
                if i + 1 < len(field) and field[i + 1][j] == '*':
                    field[i][j] += 1
                if i + 1 < len(field) and j + 1 < len(field[i]) and field[i + 1][j + 1] == '*':
                    field[i][j] += 1

    return field


def main():
    rows, cols, mins = map(int, input().split())
    coords_min = [tuple(map(int, input().split())) for _ in range(mins)]
    result = get_field_sapper(rows, cols, coords_min)

    for row in result:
        print(*row)


if __name__ == '__main__':
    main()