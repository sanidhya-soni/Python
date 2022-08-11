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
old_values = arr3d[1][1].copy()  # if we remove copy function then if we update the values then it will reflect in old_values also
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
names = np.array(['Sani', 'Rashi', 'Trump', 'Sani', 'Trump', 'Rashi', 'Sani'])
data = np.random.randint(1, 4, (7, 3))
print(data)
