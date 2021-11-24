array = [8, 5, 2, 9, 5, 6, 3]

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1
    return array

test = selectionSort(array)
print(test)