class SelectionSort:

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
            mini = i

            for j in range(i + 1, size):
                if self.array[j] < self.array[mini]:
                    mini = j

            self.swap(i, mini)
        return


# arr = [9, 8, 7, 6, 5]
# obj = SelectionSort(arr)
# obj.sort()
# print(obj.array)
