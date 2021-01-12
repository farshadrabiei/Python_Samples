def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    char = 'abcDeFGHiHklmnoP'
    grades = (81, 89, 94, 78, 61, 66, 99, 74)
    # نمایش اعداد فرد
    # odds = list(filter(filterFunc, nums))
    # print(odds)

    # نمایش حروف کوچک
    # lowers = list(filter(filterFunc2, char))
    # print(lowers)

    # به توان 2
    # squers = list(map(squareFunc, nums))
    # print(squers)

    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == '__main__':
    main()
