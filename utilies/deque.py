from collections import deque
import string


def main():
    d = deque(string.ascii_lowercase)

    print(len(d))

    for ele in d:
        print(ele.upper(), end=',')

    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    d.rotate(10)
    print(d)


if __name__ == '__main__':
    main()
