# Selection Sort

array = [5, 4, 3, 2, 1]

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

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

# test = selectionSort(array)
# print(test)

def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
    return array

test = bubbleSort(array)
print(test)
