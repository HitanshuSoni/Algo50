import re


def linearSearch(array, lengthOfArray, key):

    for i in range(0, lengthOfArray):
        if array[i] == key:
            return i
    return -1


array = [5,3,7,9,8,4,1,2]

key = 4

lengthOfArray = len(array)

result = linearSearch(array, lengthOfArray, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)