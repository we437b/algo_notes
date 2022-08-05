import sys

a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

k = 3

def quick_sort(array, rev):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    if rev:
        left, right = right, left 

    return quick_sort(left, rev) + [pivot] + quick_sort(right, rev)

a_sorted = quick_sort(a, False)
b_sorted = quick_sort(b, True)

for i in range(k):
    a_sorted[i] = b_sorted[i]

print(sum(a_sorted))
