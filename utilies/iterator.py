def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # i=iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # with open("text.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)

    # for m in days:
    #     print(m)

    # for m in range(len(days)):
    #     print(m +1, days[m])

    # for i, m in enumerate(days, start=1):
    #     print(i, m)

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], '=', m[1], 'in french')


if __name__ == "__main__":
    main()
