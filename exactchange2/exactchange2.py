if __name__ == '__main__':
    TC = int(input())
    inf = 10 ** 9
    for _ in range(TC):
        price = int(input())
        global n, coins
        n = int(input())
        coins = [int(input()) for _ in range(n)]

        dp = [[(0,0)] * (price + 1) for _ in range(n)]

        for v in range(1, price + 1):
            if v <= coins[0]:
                dp[0][v] = coins[0], 1
            else:
                dp[0][v] = inf, inf

        for i in range(1, n):
            for v in range(1, price + 1):
                dp[i][v] = dp[i - 1][v]
                take_amt = dp[i - 1][max(0, v - coins[i])][0] + coins[i]
                take_num = dp[i - 1][max(0, v - coins[i])][1] + 1
                if take_amt < dp[i][v][0] or (take_amt == dp[i][v][0] and take_num < dp[i][v][1]):
                    dp[i][v] = take_amt, take_num

        print(*dp[n - 1][price])



        