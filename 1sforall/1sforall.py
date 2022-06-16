from functools import lru_cache


@lru_cache(maxsize=1000)
def complexity(n):
    if n == 0:
        return 10**9
    if n == 1:
        return 1

    ans = 10 ** 9

    # multiplication
    v = 2
    while v * v <= n:
        if n % v == 0:
            ans = min(ans, complexity(v) + complexity(n // v))
        v += 1

    # concatenation
    for i in (10 ** k for k in range(1, 5)):
        if n > i and n % i >= i / 10:
            ans = min(ans, complexity(n // i) + complexity(n % i))

    # addition
    for i in range(n // 2 + 1):
        ans = min(ans, complexity(i) + complexity(n - i))

    return ans

# def compute(n):
#     ans = 10 ** 9

#     # multiplication
#     v = 2
#     while v * v <= n:
#         if n % v == 0:
#             ans = min(ans, memo[v] + memo[n // v])
#         v += 1

#     # concatenation
#     for i in (10 ** k for k in range(1, 5)):
#         if n > i and n % i >= i / 10:
#             ans = min(ans, memo[n // i] + memo[n % i])

#     # addition
#     for i in range(n // 2 + 1):
#         ans = min(ans, memo[i] + memo[n - i])

#     memo[n] = ans


if __name__ == '__main__':
    n = int(input())
    print(complexity(n))
    # global memo
    # memo = [0 for _ in range(n+1)]
    # memo[0], memo[1] = 10 ** 9, 1
    # for i in range(2, n+1):
    #     compute(i)
    # print(memo[n])


