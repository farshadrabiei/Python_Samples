import numpy as np
# a = np.array([3, 9, 1, 5, 7, 9, 0, 1])
# b = np.array([
#     [1, 4, 2, 9],
#     [4, 6, 1, 9],
#     [9, 8, 2, 1]])

# print(b)
# print(a[-1])
# print(b[2][1])
# print(a.ndim)
# print(b.shape)
# print(b.size)
# print(a.dtype)
# print(b.itemsize * 8)
#
# print(b.nbytes)
# a[3] =9
# print(a)

# print(a+1)
# print(a**2)

# print(b+2)
# print(b**2)

# print(a[0:4])  # ==a[:5]
# print(a[::2])
# print(a[::3])
# print(a[9::-2])
# print(a[row,column])
# print(b[:3, :2])
# print(b[:, 1])

# c = np.array([3.3, 9, 1, 5, 7, 9, 0, 1], dtype=int)
# d = np.array([3.3, 9, 1, 5, 7, 9, 0, 1], dtype=float)
# print(c)
# print(d)

###############################################################################################
# print(np.zeros([3, 4], dtype=int))
# print(np.ones([3, 4], dtype=str))
# x = 4
# b = np.arange(5, 70, 2*x-1)
# c = np.linspace(3,5,9 )
# print(b)
# print(c)


# a = np.array([3, 9, 1, 5, 7, 9]).reshape([2, 3])
# b = np.reshape(a, (2, 3))
# print(a)
# print(b)
# result
# [[3 9 1]
#  [5 7 9]]
# [[3 9 1]
#  [5 7 9]]
# a = np.array([3, 9, 1, 5, 7, 9])
# b = np.arange(1, 9, 1)
# c = np.concatenate([a, b])
# print(c)
# result [3 9 1 5 7 9 1 2 3 4 5 6 7 8]

# a = np.array([3, 1, 5, 9])
# b = np.array([3, 5, 7, 9])
# print(a == b)
# print(a > b)

# c = np.arange(1, 10)
# d = np.arange(1, 10)
# print(c, d)
# print(np.array_equal(c, d))

# a = np.array([0, 1, 1, 0])
# b = np.array([1, 1, 1, 0])
# print(np.logical_or(a, b))
# print(np.logical_and(a, b))
# print(np.logical_xor(a, b))
# print(np.logical_not(a, b))
