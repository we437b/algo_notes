# Recursive
def binary_search(array, start, end, target):

    if start > end:
        return None
    
    if len(array) == 1:
        return array[0] if array[0] == target else False

    array.sort()

    mid = int((start + end)/2)

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        end = mid - 1
    elif array[mid] < target:
        start = mid + 1
    
    return binary_search(array, start, end, target)

# Non - Recursive version, probably will be better for extreeeemely large dataset? idk
def binsearch_iter(array, target):
    
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = int((start + end)/2)
        val = array[mid]
        if val == target:
            return mid
        elif val > target:
            end = mid - 1
        elif val < target:
            start = mid + 1

    return False

arr = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]

print(binary_search(arr, 0, len(arr)-1, 13))
print(binsearch_iter(arr, 13))