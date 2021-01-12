class Person():
    def __init__(self):
        self.name = 'farshad'
        self.age = 25

    def __repr__(self):
        return "<person {0} is {1}>".format(self.name, self.age)

    def __str__(self) -> str:
        return "{0} {1}".format(self.name, self.age)

    def __bytes__(self):
        val = "Person {0}:{1}".format(self.name, self.age)
        return bytes(val.encode('utf-8'))


def main():
    cls1 = Person()
    print(repr(cls1))
    print(str(cls1))
    print("formatted {0}".format(cls1))
    print(bytes(cls1))


if __name__ == '__main__':
    main()
