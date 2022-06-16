from functools import lru_cache


@lru_cache(maxsize=None)
def dp(i, rem_tickets):
    if i == w + 1 or rem_tickets == 0:
        return 0
    ans = 0
    for price, volume in weeks[i]:
        tickets_sold = min(rem_tickets, volume)
        profit = price * tickets_sold + dp(i + 1, rem_tickets - tickets_sold)
        global first_week_price
        if profit > ans or (profit == ans and price < first_week_price):
            ans = profit
            if i == 0:
                first_week_price = price
    return ans


if __name__ == '__main__':
    n, w = list(map(int, input().split()))
    weeks = [[] for _ in range(w + 1)]
    for i in range(w + 1):
        inputs = list(map(int, input().split()))
        k = inputs[0]
        weeks[i] = list(zip(inputs[1 : k + 1], inputs[k + 1:]))

    global first_week_price
    first_week_price = 10 ** 9
    print(dp(0, n))
    print(first_week_price)
    