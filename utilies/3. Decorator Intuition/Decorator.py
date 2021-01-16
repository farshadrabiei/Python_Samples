# def favSports(s):
#     return s


# a = favSports
# print(a("Footbal"))


# def favPlayer():
#     return "Modrich"


# def favorite(func):
#     print(func())


# favorite(favPlayer)


# def favSports(x):
#     def favLayer(y):
#         return x+','+y
#     return favLayer
# favorite = favSports("Foorbal")
# print(favorite.f("Modric"))

# روش اول
# def outer(func):
#     def wrapper():
#         print("the name of my favorite player is :")
#         return func()
#     return wrapper
# def favorite():
#     print("Modric")
# fv = outer(favorite)
# fv()

# روش دوم
# def outer(func):
#     def wrapper(*args, **kwegs):
#         print("the name of my favorite player is :")
#         return func(*args, **kwegs)
#     return wrapper

# @outer
# def favorite(country):
#     print("Modric and country {}".format(country))
# favorite("brazil")

import time


def time_it(func):
    def wrapper_func(*args, **keyword):
        start = time.time()
        result = func(*args, **keyword)
        end = time.time()
        total = (end-start) * 1000
        print(func.__name__ + "Took" + str(total))
        return result
    return wrapper_func


@time_it
def evenNo(number):
    eList = []
    for x in range(0, number):
        if x % 2 == 0:
            eList.append(x)
    return eList


@time_it
def oddNo(number):
    dList = []
    for x in range(0, number):
        if x % 2 != 0:
            dList.append(x)
    return dList


event = evenNo(10000)
odd = oddNo(10000)
