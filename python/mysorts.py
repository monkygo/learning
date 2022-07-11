

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

def bubbleSort2(arr):
    arrLen = len(arr)
    if arrLen == 0:
        return
    # repeat n - 1, since n - 1 steps are needed
    # to move to correct location in worst case.
    # if no swaps made in a round, then you won't
    # make another swap in the next round.
    swapped = False
    for i in range(arrLen - 1):
        for j in range(arrLen - 1):
            if arr[j] > arr[j+1]:
                swapped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if swapped == False:
            break
    return arr

arr1 = [5,7,9,4,2,8,6,9,7,1]
arr2 = [1]
arr3 = [2,3]
arr4 = []
print(bubbleSort(arr1))
print(bubbleSort(arr2))
print(bubbleSort(arr3))
print(bubbleSort(arr4))

arr1 = [5,7,9,4,2,8,6,9,7,1]
arr2 = [1]
arr3 = [2,3]
arr4 = []
print(bubbleSort2(arr1))
print(bubbleSort2(arr2))
print(bubbleSort2(arr3))
print(bubbleSort2(arr4))

# how to do merge sort???
# split the array into two left and right halves
# until ony a single element then return.
# merge the left and right of the returned arrays.

# writing merge algo
def mergeSort(arr):
    arrLen = len(arr)
    if arrLen < 2:
        return
    mid = arrLen // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i=j=k = 0
    m = len(left)
    n = len(right)
    while i < m and j < n:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1

arr1 = [5,7,9,4,2,8,6,9,7,1]
arr2 = [1]
arr3 = [2,3]
arr4 = []
mergeSort(arr1)
mergeSort(arr2)
mergeSort(arr3)
mergeSort(arr4)
print(arr1)
print(arr2)
print(arr3)
print(arr4)


