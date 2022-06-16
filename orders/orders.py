def fill_dp():
    curr_w = 0
    while curr_w <= c:
        dp[0][curr_w] = 1
        curr_w += cost[0]
    for i in range(1, n):
        for w in range(c + 1):
            curr_w = 0
            while curr_w <= w:
                dp[i][w] += dp[i - 1][w - curr_w]
                curr_w += cost[i]

def print_items(order_cost):
    items = []
    for i in range(n - 1, 0, -1):
        if order_cost == 0:
            break
        while dp[i - 1][order_cost] == 0:
            order_cost -= cost[i]
            items.append(i + 1)
    while order_cost > 0:
        order_cost -= cost[0]
        items.append(1)

    items.reverse()
    print(*items)



if __name__ == '__main__':
    n = int(input())
    cost = list(map(int, input().split()))
    m = int(input())
    orders = list(map(int, input().split()))
    c = max(orders)

    dp = [[0] * (c + 1) for _ in range(n)]
    fill_dp()
    for order in orders:
        if dp[n - 1][order] == 0:
            print('Impossible')
        elif dp[n - 1][order] == 1:
            print_items(order)
        else:
            print('Ambiguous')
