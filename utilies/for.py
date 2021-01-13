matrix = [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
         ]

flat = [num for row in matrix for num in row]
# flat = []
# for row in matrix:
#       for num in row:
#           flat.append(num)
print(flat)

sum([i * i for i in range(1000)]) ==  sum(map(lambda i: i*i, range(1000)))

def f(x,y):
    return x,y
print(list([ f(m,i) for i in (t1,t2) for m in i]))
