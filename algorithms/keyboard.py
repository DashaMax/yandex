def get_button_click(buttons: list) -> dict:
    button_click = {}

    for button in buttons:
        if button not in button_click:
            button_click[button] = 1
        else:
            button_click[button] += 1

    return button_click


def is_broken(d: dict, clicks: list, n: int) -> str:
    if d[n + 1] > clicks[n]:
        return 'YES'
    return 'NO'


def main():
    n, c, k, p = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
    button_click = get_button_click(p)

    for i in range(n):
        print(is_broken(button_click, c, i))


if __name__ == '__main__':
    main()