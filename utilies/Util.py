#utility
def main():
    lst1 = [1,-2,3,0,5,6]

    print(any(lst1))

    #در صورتی که تمامی توالی درست باشد
    print(all(lst1))

    print("min : ",min(lst1))

    print("max : ",max(lst1))

    print("sum : ",sum(lst1))


if  __name__ == "__main__":
    main()
