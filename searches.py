


def binarySearch(arr, x):
    foundIndex = -1
    sIndex = 0
    eIndex = len(arr) - 1

    while foundIndex == -1 and (eIndex - sIndex) >= 0:
        mid = eIndex + sIndex // 2
        if x < arr[mid]:
            eIndex = mid - 1
        elif x > arr[mid]:
            sIndex = mid + 1
        else:
            foundIndex = mid

    return foundIndex

def binarySearch2(arr, x):
    return bSearch2(arr, x, -1, 0, len(arr) - 1)

def bSearch2(arr, x, foundIndex, sIndex, eIndex):
    if foundIndex != -1 or (eIndex - sIndex) < 0:
        return foundIndex
    mid = eIndex + sIndex // 2
    if x < arr[mid]:
        eIndex = mid - 1
    elif x > arr[mid]:
        sIndex = mid + 1
    else:
        foundIndex = mid

    return bSearch2(arr, x, foundIndex, sIndex, eIndex)

arr = [1,2,3,4,5,6,7]
print(binarySearch(arr, 6))

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,20]
print(binarySearch(arr, 18))

print(binarySearch(arr, 20))

print(binarySearch(arr, 22))

print(binarySearch(arr, 0))

print(binarySearch(arr, 9))

print(binarySearch(arr, 10))
print(binarySearch(arr, 11))
print(binarySearch(arr, 3))


print(binarySearch2(arr, 18))