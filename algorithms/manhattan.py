from random import randint
from time import time


def get_coords_t(t: int, coords: tuple) -> set:
    coords_t = set()

    for i in range(-t, t + 1):
        for j in range(-t, t + 1):
            if abs(i) + abs(j) <= t:
                coords_t.add((coords[0] + i, coords[1] + j))

            # coords_t.add((coords[0] - t + i, coords[1] - j))
            # coords_t.add((coords[0] - t + i, coords[1] + j))
            # coords_t.add((coords[0] + t - i, coords[1] - j))
            # coords_t.add((coords[0] + t - i, coords[1] + j))

    return coords_t


def get_coords_d(d: int, coords: tuple) -> set:
    coords_d = set()

    for i in range(-d, d + 1):
        for j in range(-d, d + 1):
            if abs(i) + abs(j) <= d:
                coords_d.add((coords[0] + i, coords[1] + j))

    return coords_d


def get_coords(t: int, d: int, a: list) -> set:
    coords_t = get_coords_t(t, (0, 0))
    # print('t:', coords_t)

    for i in range(len(a)):
        coords_d = get_coords_d(d, a[i])
        # print('d:', coords_d)

        coords = coords_t & coords_d
        # print('&:', coords)

        if i == len(a) - 1:
            return coords

        max_sum = sorted(coords, key=lambda x: abs(x[0]) + abs(x[1]), reverse=True)[0]
        print(max_sum)
        coords_border = []

        for coord in coords:
            if abs(coord[0] + coord[1]) == max_sum:
                coords_border.append(coord)

        # minx = min(coords, key=lambda x: x[0])[0]
        # maxx = max(coords, key=lambda x: x[0])[0]
        # miny = min(coords, key=lambda x: x[1])[1]
        # maxy = max(coords, key=lambda x: x[1])[1]
        #
        # coords_border = list(filter(lambda x: x[0] == minx or x[0] == maxx or x[1] == miny or x[1] == maxy, coords))
        coords_t = set(coords_border)
        # print('borders:', coords_t)

        for coord in coords_border:
            coords_t |= get_coords_t(t, coord)

        # print('t', coords_t)


def main():
    t, d, n = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    result = get_coords(t, d, coords)

    # t, d, n = randint(1, 2), randint(1, 2), randint(3, 5)
    # coords = [(randint(-3, 3), randint(-3, 3)) for _ in range(n)]
    # print(t, d, n)
    # print(coords)
    #
    # time_start = time()

    print(len(result))

    for coord in result:
        print(*coord)

    # print(time() - time_start)


if __name__ == '__main__':
    main()