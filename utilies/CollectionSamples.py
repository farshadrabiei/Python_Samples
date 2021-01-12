# list
# tuple
# set
# dictionary


# namedtuple
# orderedDict
# defaultdict
# Counter
# deque

import collections


def main():
    Point = collections.namedtuple("Point", "x y z")
    p1 = Point(10, 20, 40)
    p2 = Point(20, 30, 50)
    print(p1, p2)
    print(p1.x)

    p1 = p1._replace(x=100)

    print(p1)

    # Error
    # p1.x = 11
    # print(p1)


def dic():

    pass


if __name__ == '__main__':
    dic()
    main()
