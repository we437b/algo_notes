# Probably O(n^2)

n = int(input())
vaults = list(map(int, input().split()))


best = [0] * n
i = 0
total = 0

best[0] = vaults[0]
best[1] = max(vaults[0], vaults[1])

#Dynamic Programming, best solution until i'th vault
for i in range(2, n):
    best[i] = max(best[i-1], (best[i-2] + vaults[i]))


print(best[n-1])