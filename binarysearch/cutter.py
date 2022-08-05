
# Problem Conditions
req = -1
rods = []

# a : cutter height
# b : requested amount
def eval(arr, a):
    return sum(list(map(lambda x: x - a if x > a else 0, arr)))

req = int(input())
rods = list(map(int, input().split()))

start = 0
max_int = max(rods)
heights = [i for i in range(max_int)]

ret = 0

while start <= max_int:
    
    mid = int((start + max_int)/2)
    height = heights[mid]
    supply = eval(rods, height)
    
    if supply == req:
        ret = max(height, ret)
        break
    elif supply > req:
        ret = max(height, ret)
        start = mid + 1
    elif supply < req:
        max_int = mid - 1

print(ret)

