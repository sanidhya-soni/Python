import numpy as np

data1 = [1, 2, 4, 7, 8.5]
data2 = [1, 2, 4, 7, 8.5]
np_data = np.array([data1, data2])
print(np_data)

print((type(np_data)))

np_zeros = np.zeros(10)
print(np_zeros)

np_ones = np.ones((2, 5), dtype=np.int32)
print(np_ones)

np_empty = np.empty((4, 2, 2))
print(np_empty)

np_arrange = np.arange(7)  # can give a range also np.arange(7, 10)
print(np_arrange)

np_full = np.full(7, 2, dtype=np_arrange.dtype)
print(np_full)

np_eye = np.identity(2)  # identity makes only N X N while eye can make 2 X 5 also with first diagonal as 1 and rest 0
print(np_eye)

print(np_ones.dtype)

np_strings = np.array(['1.25', '5.6', '83.9'])
np_strings_to_float = np_strings.astype(np.float64)  # we can write float also instead of np.float64
print(np_strings_to_float)

# Arithmetic operations on array using numpy

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr * arr)
print(arr * 2)
print(1 / arr)
print(arr + 2)

# Indexing and Slicing
# 1D
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[:] = 23
print(arr)
arr[5:8] = 20
print(arr)
arr[:] = 10
print(arr)

# 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[[2]])
print(arr2d[1][1])

# 3D
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[1][1])
old_values = arr3d[1][
    1].copy()  # if we remove copy function then if we update the values then it will reflect in old_values also
arr3d[1][1] = 25
print(arr3d[1])
arr3d[1][1] = old_values
print(arr3d[1])

# Slicing multidimensional arrays
print(arr2d[:2])
print(arr2d[:2, 1:])

# Slicing with index included
print(arr2d[1, :2])

print(arr3d[1:, :1, 1:])

# Boolean Indexing
names = np.array(['Sani', 'Rashi', 'Trump', 'Sani', 'Trump', 'Rashi', 'Sanidhya'])
# data = np.random.randint(1, 11, (5, 3))  # randint(lower_limit, upper_limit, ()tuple for 2d or 3d array)
data = np.random.randn(7, 4)  # Keep length same as that of boolean array
print(data)
print(names == 'Sani')
print(data[names == 'Sani'])
print(data[names == 'Sani', 2:])
print(data[names == 'Sani', 3])  # 3rd column will be selected

print(~(names == 'Sani'))  # ~ can be used instead of ! hence '!=' == ~(condition)
print(data[~(names == 'Sani')])

print((names == 'Sani') | (names == 'Rashi'))
print(data[(names == 'Sani') | (names == 'Rashi')])

# Setting values by boolean indexing
data[data < 0] = 0
print(data)

data[names != 'Rashi'] = 7
print(data)

# Fancy Indexing - Indexing using integer array
arr = np.empty((8, 4))
# print(arr)
for i in range(8):
    arr[i] = i
print(arr)
print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])  # Its like select following columns in this order

# Transpose of a Matrix
arr = np.arange(15).reshape((5, 3))
print(arr)
print(arr.T)

# Dot Product
arr = np.random.randn(6, 3)
print(arr)
print(np.dot(arr.T, arr))

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1, 0, 2)))  # Just reorder the axes in the tuple

# Swap Axes
print(arr.swapaxes(1, 2))

# Universal Functions: Fast Element wise Array Functions
arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))

x = np.random.randn(8)
print(x)
y = np.random.randn(8)
print(y)
print(np.maximum(x, y))

arr = np.random.randn(8) * 5
print(arr)

remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

# Array-Oriented Programming with Arrays
points = np.arange(-5, 5, 0.01)
print(points)
xs, ys = np.meshgrid(points, points)
# print(xs)
print(ys)

# Understanding
# px = np.arange(1, 101)
# py = np.arange(1, 101)
# print(np.meshgrid(px, py))

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.show()
