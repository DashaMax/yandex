def event_handler(n: int, m: int, q: int) -> list:
    result = []
    data = {str(key + 1): [1] * m + [0] for key in range(n)}

    for _ in range(q):
        event = input().split()

        if event[0] == 'DISABLE':
            data[event[1]][int(event[2]) - 1] = 0

        elif event[0] == 'RESET':
            data[event[1]][-1] += 1
            data[event[1]][:m] = [1] * m

        elif event[0] == 'GETMAX':
            max_ = max(data.items(), key=lambda x: sum(x[1][:m]) * x[1][-1])
            result.append(max_[0])

        elif event[0] == 'GETMIN':
            min_ = min(data.items(), key=lambda x: sum(x[1][:m]) * x[1][-1])
            result.append(min_[0])

    return result


def main():
    n, m, q = map(int, input().split())
    result = event_handler(n, m, q)

    for i in result:
        print(i)


if __name__ == '__main__':
    main()

