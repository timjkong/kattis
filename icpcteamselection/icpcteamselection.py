if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        N = int(input())
        scores = list(map(int, input().split()))
        scores.sort()
        S = 0
        for i in range(3 * N - 2, N - 1, -2):
            S += scores[i]
        print(S)

