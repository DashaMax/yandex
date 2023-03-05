def main():
    n = int(input())
    const = asc = asc_weak = desc = desc_weak = 0
    i = -1
    later = first = n

    while n != -2 * 10 ** 9:
        if i > -1:
            if n == first == later:
                const += 1

            if n > later >= first:
                asc += 1

            if n >= later >= first:
                asc_weak += 1

            if n < later <= first:
                desc += 1

            if n <= later <= first:
                desc_weak += 1

        i += 1
        later = n
        n = int(input())

    if i == const:
        print('CONSTANT')
    elif i == asc:
        print('ASCENDING')
    elif i == asc_weak:
        print('WEAKLY ASCENDING')
    elif i == desc:
        print('DESCENDING')
    elif i == desc_weak:
        print('WEAKLY DESCENDING')
    else:
        print('RANDOM')


if __name__ == '__main__':
    main()