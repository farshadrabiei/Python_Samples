from collections import OrderedDict


def main():
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                  ("Cadinals", (20, 10)), ("dragons", (22, 8)),
                  ("kings", (15, 15)), ("charges", (20, 10)),
                  ("jets", (16, 14)), ("Warriors", (25, 5))]

    sportTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    teams = OrderedDict(sportTeams)

    print(teams)

    tm, wl = teams.popitem(False)

    print("Top team :", tm, wl)

    for i, item in enumerate(teams, start=1):
        print(i, item)
        if(i == 4):
            break

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print(a == b)


if __name__ == '__main__':
    main()
