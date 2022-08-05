from numpy import c_


to_sort = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# Selection Sort

print("---------------Selection Sort---------------")
selection_sorted = to_sort.copy()
for i in range(len(selection_sorted)-1):
    temp = selection_sorted[i]
    min_idx = selection_sorted.index(min(selection_sorted[i:]))
    selection_sorted[i] = selection_sorted[min_idx]
    selection_sorted[min_idx] = temp
    print(selection_sorted)

    
# Insertion Sort
print("---------------Insertion Sort---------------")
insertion_sorted = to_sort.copy()
for i in range(1, len(insertion_sorted)):
    cur_loc = i
    for j in range(i, 0, -1):
        if insertion_sorted[j] < insertion_sorted[j-1]:
            insertion_sorted[j], insertion_sorted[j-1] = insertion_sorted[j-1], insertion_sorted[j]
            print(insertion_sorted)

# Quick Sort
print("---------------Quick Sort---------------")
quick_sorted = to_sort.copy()
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(quick_sorted))
    
# Counting Sort
print("---------------Counting Sort---------------")
c_sorted = to_sort.copy()
max_int = max(c_sorted) + 1
count = [0] * max_int
arr = []

for i in c_sorted:
    count[i] += 1

for i in range(max_int):
    for j in range(count[i]):
        arr.append(i)

print(arr)
        
        
        