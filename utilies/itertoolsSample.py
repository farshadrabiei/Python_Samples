import itertools


def testFun(x):
    return x < 40


def main():
    seq1 = ["Joe", "John", "Mike"]
    vlas = [10, 20, 30, 40, 50, 40, 30, 5]

    print(list(itertools.dropwhile(testFun, vlas)))
    print(list(itertools.takewhile(testFun, vlas)))

    # cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # count1 = itertools.count(100, 10)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # acc = itertools.accumulate(vlas, max)
    # print(list(acc))

    # x = itertools.chain("ABCD", "1234")
    # print(list(x))


if __name__ == '__main__':
    main()
