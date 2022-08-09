
# number of kinds of currency
N = 3
# Total value of currency to represent
M = 7
# List of currencies
curren = [2, 3, 5]

# memoization for dp
memo = [0] * (max(M, max(curren)) + 1)
for i in curren:
    memo[i] = 1

def getcurrency(num):

    if num == 0:
        return 0

    if num < 0:
        return -1000000

    if memo[num] != 0:
        return memo[num]
    else:
        cur_list = [getcurrency(num - j) for j in curren if getcurrency(num - j) > 0]
        if not cur_list:
            return -100000
        coins = 1 + min(cur_list)
        memo[num] = coins
        return coins

    

res = getcurrency(M)
print(res if res > 0 else -1)