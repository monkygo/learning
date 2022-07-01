
from cgitb import small


def selectionSort(arr):
    arrLen = len(arr)
    if arrLen == 0:
        return
    smallest = 0
    for i in range(arrLen):
        for j in range(i + 1, arrLen):
            if arr[j] < arr[smallest]:
                smallest = j
        # swap once we finish j loop
        # swamp location with the smallest
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        # move the smallest index to next i
        smallest = i  + 1
    return arr

arr1 = [5,7,9,4,2,8,6,9,7,1]
arr2 = [1]
arr3 = [2,3]
arr4 = []
print(selectionSort(arr1))
print(selectionSort(arr2))
print(selectionSort(arr3))
print(selectionSort(arr4))
        
def bubbleSort(arr):
    arrLen = len(arr)
    if arrLen == 0:
        return
    cnt = 0
    for i in range(arrLen):
        for j in range(1, arrLen - cnt):
            if arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
        cnt += 1
    return arr
arr1 = [5,7,9,4,2,8,6,9,7,1]
arr2 = [1]
arr3 = [2,3]
arr4 = []
print(bubbleSort(arr1))
print(bubbleSort(arr2))
print(bubbleSort(arr3))
print(bubbleSort(arr4))