# max 1D range sum

if __name__ == '__main__':
    n, p = map(int, input().split())
    profit = list(map(lambda x: int(x) - p, input().split()))

    curr_sum, max_profit = 0, 0
    for x in profit:
        curr_sum += x
        max_profit = max(max_profit, curr_sum)
        curr_sum = max(0, curr_sum)
    
    print(max_profit)
