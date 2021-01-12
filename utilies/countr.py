from typing import Counter


def main():
    class1 = ["Bob", "Jams", "Jams"]
    class2 = ["Bill", "Jams", "Joe"]
    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["Jams"])

    print(sum(c1.values()), "in clas 1")

    c1.update(class2)
    print(sum(c1.values()), "in clas 1")

    print(c1.most_common(3))

    c1.subtract(class2)
    print(c1.most_common(3))

    print(c1 & c2)


if __name__ == '__main__':
    main()
