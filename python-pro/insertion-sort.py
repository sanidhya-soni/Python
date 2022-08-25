class InsertionSort:

    array = []

    def __init__(self, array):
        self.array = array

    def swap(self, a, b):
        if a == b:
            return

        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def sort(self):
        size = len(self.array)
        for i in range(size):
            temp = self.array[i]
            for j in range(i - 1, -1):
                if temp < self.array[j]:
                    self.array[j + 1] = self.array[j]
                else:
                    break
                self.array[j + 1] = temp

arr = [9, 8, 7, 6, 5]
obj = InsertionSort(arr)
obj.sort()
print(obj.array)
