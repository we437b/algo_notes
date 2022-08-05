from bisect import bisect_left, bisect_right
from re import M

vals = int(input())
arr = list(map(int, input().split()))

left = bisect_left(arr, vals)
right = bisect_right(arr, vals)

print(right - left)
    