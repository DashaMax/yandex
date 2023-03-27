def get_sales(a: list) -> dict:
    buyers = {}

    for buyer in a:
        buyer = buyer.split()

        if buyer[0] not in buyers:
            buyers[buyer[0]] = {buyer[1]: int(buyer[2])}
        elif buyer[1] not in buyers[buyer[0]]:
            buyers[buyer[0]][buyer[1]] = int(buyer[2])
        else:
            buyers[buyer[0]][buyer[1]] += int(buyer[2])

    return buyers


def main():
    with open('input.txt') as file:
        text = file.readlines()
    result = get_sales(text)

    for buyer in sorted(result.items()):
        print(f'{buyer[0]}:')
        for product in sorted(buyer[1].items()):
            print(*product)


if __name__ == '__main__':
    main()