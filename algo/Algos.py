# Algos

# Selection Sort

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        for i in range(currentIdx + 1, len(array)):
            smallestIdx = currentIdx
            if array[i] < array[smallestIdx]:
                array[i], array[smallestIdx] = array[smallestIdx], array[i]
        currentIdx += 1
    return(array)


def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1
    return(array)

array = [4, 3, 2, 1, 5]
# result = selectionSort(array)
result = bubbleSort(array)
print(result)