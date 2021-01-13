class Employee():
    def __init__(self, fname, lname, level, yrsseniority):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsseniority

        # self >= other
    def __ge__(self, other):
        if(self.level == other.level):
            return self.seniority >= other.seniority
        return self.level >= other.level
        # self >  other

    def __gt__(self, other):
        if(self.level == other.level):
            return self.seniority > other.seniority
        return self.level > other.level
        # self <   other

    def __lt__(self, other):
        if(self.level == other.level):
            return self.seniority > other.seniority
        return self.level < other.level
        # self <=  other

    def __le__(self, other):
        if(self.level == other.level):
            return self.seniority <= other.seniority
        return self.level <= other.level

        # self ==  other
    def __eq__(self, other):
        pass

       # self !=  other
    def __ne__(self, other):
        pass


def main():
    dept = []
    dept.append(Employee("Farshad", "Rabiei", 5, 9))
    dept.append(Employee("Reza", "hmadi", 4, 12))
    dept.append(Employee("Omid", "Vafa", 5, 13))

    print(dept[0] > dept[1])
    print(dept[1] < dept[2])
    print(dept[0] > dept[2])

    emps = sorted(dept)

    for m in emps:
        print(m.lname)


if __name__ == '__main__':
    main()
