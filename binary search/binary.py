def binarySearch(array, key, low, high):

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [1,2,3,4,5,6,7,8,9,10]

key = 9

result = binarySearch(array, key, 0, len(array)-1)

if result != -1:
    print("Element is present at index: ", result)
else:
    print("Not Found")
