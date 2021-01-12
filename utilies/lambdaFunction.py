from iterator import main


def cel(temp):
    return (temp * 9/5)+32


def far(temp):
    return (temp-32) * 5/9


def main():
    ctemp = [0, 12, 34, 100]
    ftemp = [32, 65, 100, 212]

    print(list(map(cel, ctemp)))
    print(list(map(cel, ftemp)))

    print(list(map(lambda t: (t * 9/5)+32, ctemp)))
    print(list(map(lambda t: (t-32) * 5/9, ftemp)))


if __name__ == '__main__':
    main()
