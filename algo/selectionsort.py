# array = [6, 2, 1, 9, 8, 7]
# array[2], array[3] = array[3], array[2]
# print(array)

# O(n^2) time / O(1) space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Test

array = [26, 11, 21, 20, 17, 12, 10]
result = selectionSort(array)
print(result)