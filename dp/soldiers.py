N = int(input())

soldiers = list(map(int, input().split()))
# reversing to make it longest increasing
soldiers.reverse()

dp = [1] * (len(soldiers) + 1)

for i in range(len(soldiers)):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(soldiers) - max(dp))
