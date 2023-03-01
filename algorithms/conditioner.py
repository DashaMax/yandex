from random import randint
from time import time


def get_temp(tr: int, tc: int, mode: str) -> int:
    if mode == 'freeze' and tr <= tc:
        return tr
    elif mode == 'freeze' and tr > tc:
        return tc
    elif mode == 'heat' and tr >= tc:
        return tr
    elif mode == 'heat' and tr < tc:
        return tc
    elif mode == 'fan':
        return tr
    else:
        return tc


def main():
    time_start = time()

    modes = ('freeze', 'heat', 'auto', 'fan')
    mode = modes[randint(0, 3)]
    t_room, t_cond = randint(-50, 50), randint(-50, 50)
    print(t_room, t_cond, mode)

    temp = get_temp(t_room, t_cond, mode)
    print(temp)

    time_end = time()
    print(time_end - time_start)


def test():
    assert get_temp(10, 20, 'freeze') == 10
    assert get_temp(10, 10, 'freeze') == 10
    assert get_temp(20, 10, 'freeze') == 10
    assert get_temp(-20, -30, 'freeze') == -30
    assert get_temp(0, 10, 'freeze') == 0

    assert get_temp(10, 20, 'heat') == 20
    assert get_temp(10, 10, 'heat') == 10
    assert get_temp(20, 10, 'heat') == 20
    assert get_temp(-20, 0, 'heat') == 0

    assert get_temp(10, 20, 'fan') == 10
    assert get_temp(10, 10, 'fan') == 10
    assert get_temp(20, 10, 'fan') == 20
    assert get_temp(-20, 0, 'fan') == -20

    assert get_temp(10, 20, 'auto') == 20
    assert get_temp(10, 10, 'auto') == 10
    assert get_temp(20, 10, 'auto') == 10
    assert get_temp(-20, 0, 'auto') == 0


if __name__ == '__main__':
    main()
