if __name__ == '__main__':
    n = int(input())
    weights = [int(input()) for _ in range(n)]

    LIS, LDS = [1] * n, [1] * n
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if weights[i] < weights[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
            else:
                LDS[i] = max(LDS[i], LDS[j] + 1)
        ans = max(ans, LIS[i] + LDS[i] - 1)
    print(ans)

    