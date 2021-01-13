

def main():
    # list(map(func,arry))
    # r1 = list(map(lambda t: t**2, [1, 2, 3, 4, 5]))
    # print(r1)

    # r2 = [t**2 for t in [1, 2, 3, 4, 5]]

    # print(r2)

    ctemp = [0, 12, 34, 100]

    tempDict = {t: (t*9/5) + 32 for t in ctemp if t < 100}

    print(tempDict)
    print(tempDict[12])

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 54, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Smith": 4}

    newTeam = {k: v for k in team1 for k, v in team1.items() if v > 25}
    print(newTeam)

    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)

    ctemp = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    ftemp1 = [(t * 9/5) + 32 for t in ctemp]
    ftemp2 = {(t * 9/5) + 32 for t in ctemp}

    print(ftemp1)
    print(ftemp2)

    print(ftemp1[0])
    # print(ftemp2[0])

    sTem = "The Quick brown fox over the lazy dog"

    chars = {c.upper() for c in sTem if not c .isspace()}

    print(list(chars))
    # for i, k in enumerate(list(chars)):
    #     print(i, k)

    test_set = set("geEks")
    com = [print(val) for val in test_set]


if __name__ == '__main__':

    main()
