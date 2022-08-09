T = int(input())

DIMENSIONS = []
VALUES = []
# Processing inputs
for i in range(T):
    dimension = list(map(int, input().split()))
    vals_raw = list(map(int, input().split()))

    ind = 0

    vals = []

    for i in range(dimension[0]):
        row = []
        for j in range(dimension[1]):
            row.append(vals_raw[ind])
            ind += 1
        vals.append(row)
    
    DIMENSIONS.append(dimension)
    VALUES.append(vals)

# Update array with max possible previous value

for mine in VALUES:
    dimension = DIMENSIONS[VALUES.index(mine)]
    
    for j in range(dimension[1]):
        for i in range(dimension[0]):
            if j == 0:
                continue
            else:
                max_prev = 0
                delta = [-1, 0, 1]
                for k in delta:
                    pos = i + k
                    if 0 <= pos < dimension[0]:
                        max_prev = max(max_prev, mine[i][j] + mine[pos][j-1])
                mine[i][j] = max_prev
    
    print(max([i[-1] for i in mine]))
    