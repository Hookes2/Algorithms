# BubbleSort

from algo.selectionsort import swap


def bubbleSort(array):
    isSorted = False
    while not isSorted:
        for i in len(array) - 1:
            if array[i] > array[i + 1]:
                swap(i + 1, i, array)
        isSorted = True
    return(array)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [5, 4, 3, 2, 1]
result = bubbleSort(array)
print(result)