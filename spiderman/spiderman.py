from functools import lru_cache


INF = 10 ** 9

@lru_cache(maxsize=None)
def dp(i, curr_height):
    if curr_height < 0:
        return (INF, '')
    if i == m:
        return (0 if curr_height == 0 else INF, '')
    up_dist, up_path = dp(i + 1, curr_height + dist[i])
    down_dist, down_path = dp(i + 1, curr_height - dist[i])
    if up_dist < down_dist:
        return (max(curr_height, up_dist), 'U' + up_path)
    return (max(curr_height, down_dist), 'D' + down_path)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = int(input())
        dist = list(map(int, input().split()))
        total_dist, path = dp(0, 0)
        print('IMPOSSIBLE' if total_dist == INF else path)
        dp.cache_clear()
        