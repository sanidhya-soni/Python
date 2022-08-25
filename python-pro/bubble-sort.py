class BubbleSort:

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

        for i in range(0, size - 1):
            for j in range(0, size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.swap(j, j + 1)

        return

# arr = [9, 8, 7, 6, 5]
# obj = BubbleSort(arr)
# obj.sort()
# print(obj.array)
