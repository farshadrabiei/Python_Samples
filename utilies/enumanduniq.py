from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    Apple = 1
    Banana = 2,
    Oange = 3,
    Tomato = 4
    # Red_de =1 ==>errror
    PEAR = auto()


def main():
    print(Fruit.Oange)
    print(type(Fruit.Oange))
    print(repr(Fruit.Oange))
    print(Fruit.PEAR.name, Fruit.PEAR.value)
    myFruits = {}
    myFruits[Fruit.Banana] = "M farshad"
    print(myFruits[Fruit.Banana])


if __name__ == '__main__':
    main()
