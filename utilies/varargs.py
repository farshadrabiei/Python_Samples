

def additional(base, *args):
    result = 0
    for arg in args:
        result += arg
    return result


def myFunc(arg1, arg2, *, suppress=False):
    pass


def main():
    print(additional(10, 20, 30, 40))
    myNums = [5, 10, 15, 20]
    # به نحوه ارسال آرایه دقت شود
    print(additional(*myNums))


if __name__ == '__main__':
    main()
    myFunc(1, 2, suppress=True)
