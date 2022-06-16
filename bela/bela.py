if __name__ == '__main__':
    dominant_values = {'A' : 11, 
                       'K' : 4, 
                       'Q' : 3,
                       'J' : 20,
                       'T' : 10,
                       '9' : 14,
                       '8' : 0,
                       '7' : 0}

    non_dominant_values = {'A' : 11,
                           'K' : 4,
                           'Q' : 3,
                           'J' : 2,
                           'T' : 10,
                           '9' : 0,
                           '8' : 0,
                           '7' : 0}

    n, dominant_suit = input().split()
    n = int(n)
    ans = 0
    for _ in range(4 * n):
        card, suit = list(input())
        ans += dominant_values[card] if suit == dominant_suit else non_dominant_values[card]
    print(ans)