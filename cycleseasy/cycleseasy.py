from functools import lru_cache
import math

def LSOne(S):
    return S & (-S)

@lru_cache(maxsize=None)
def dp(u, mask):
    if mask == 0:
        return 0 if is_forbidden[u][0] else 1
    ans = 0
    m = mask
    while m:
        two_pow_v = LSOne(m)
        v = int(math.log2(two_pow_v)) + 1
        if not is_forbidden[u][v]:
            ans += dp(v, mask ^ two_pow_v)
        m -= two_pow_v
    return ans


if __name__ == '__main__':
    T = int(input())
    for TC in range(1, T + 1):
        global n, is_forbidden
        n, k = list(map(int, input().split()))
        is_forbidden = [[0] * n for _ in range(n)]
        for _ in range(k):
            u, v = list(map(int, input().split()))
            is_forbidden[u - 1][v - 1] = 1
            is_forbidden[v - 1][u - 1] = 1
        num_cycles = dp(0, (1 << (n - 1)) - 1) // 2
        print(f'Case #{TC}: {num_cycles % 9901}')
        dp.cache_clear()
