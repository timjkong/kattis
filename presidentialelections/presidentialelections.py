'''
For each state, number of voters required = max(0, ceil((F + C + U) / 2) - C)
Find min voters required (values) s.t. delegates (weights) >= delegates required
'''

from math import ceil

inf = 2*(10**9)

def min_knapsack():
    # let dp[i][w] be min value required for min weight of w
    n = len(weight)
    required = c_delegates_required - c_delegates_confirmed
    dp = [[inf] * (required + 1) for _ in range(s)]
    for w in range(min(required, weight[0]) + 1):
        dp[0][w] = value[0]
    for i in range(1, n):
        for w in range(required + 1):
            dp[i][w] = dp[i - 1][w]
            if weight[i] >= w:
                dp[i][w] = min(dp[i][w], value[i])
            else:
                dp[i][w] = min(dp[i][w], dp[i - 1][w - weight[i]] + value[i])
    
    return dp[n - 1][required]


if __name__ == '__main__':
    s = int(input())
    value, weight = [], []
    total_delegates, f_delegates_confirmed, c_delegates_confirmed = (0,) * 3
    for _ in range(s):
        d, c, f, u = list(map(int, input().split()))
        total_delegates += d
        c_voters_required = (f + c + u) // 2 + 1
        f_voters_required = ceil((f + c + u) / 2)
        if f >= f_voters_required:
            f_delegates_confirmed += d
            continue
        if c >= c_voters_required:
            c_delegates_confirmed += d
            continue
        value.append(c_voters_required - c)
        weight.append(d)

    c_delegates_required = total_delegates // 2 + 1
    f_delegates_required = ceil(total_delegates / 2)
    if c_delegates_confirmed >= c_delegates_required:
        print(0)
    elif f_delegates_confirmed >= f_delegates_required:
        print('impossible')
    else:
        print(min_knapsack())

    
        
